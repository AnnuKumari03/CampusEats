from functools import wraps
import gzip
import hashlib
import json
import os
import time
import uuid

from flask import Flask, Response, jsonify, request

import store
from errors import problem
from payments_client import charge_with_retry, CardDeclined, PaymentsUnavailable

app = Flask(__name__)
ALLOWED_STATUSES = {"pending", "confirmed", "cancelled"}
ALLOWED_SORTS = {"id", "createdAt", "amount"}
RATE_LIMIT = int(os.environ.get("RATE_LIMIT", "60"))
_RATE = {}
_IDEMPOTENCY_RESULTS = {}


def _client_id():
    return request.headers.get("Authorization", "anonymous") or "anonymous"


def _rate_limit():
    now = time.time()
    client = _client_id()
    bucket = _RATE.setdefault(client, {"start": now, "count": 0})
    if now - bucket["start"] >= 60:
        bucket["start"] = now
        bucket["count"] = 0
    bucket["count"] += 1
    remaining = max(RATE_LIMIT - bucket["count"], 0)
    if bucket["count"] > RATE_LIMIT:
        return False, remaining
    return True, remaining


def _accepts_json():
    accept = request.headers.get("Accept", "application/json")
    return "*/*" in accept or "application/json" in accept


def _require_json():
    if request.method in {"POST", "PUT", "PATCH"}:
        content_type = request.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            return problem(400, "invalid-request", "Content-Type must be application/json")
    if not _accepts_json():
        return problem(406, "not-acceptable", "Only application/json is supported")
    return None


def _bearer_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        value = request.headers.get("Authorization", "")
        if not value.startswith("Bearer ") or not value[7:].strip():
            return problem(401, "unauthorized", "Authorization: Bearer <token> is required")
        return fn(*args, **kwargs)
    return wrapper


def _etag(order):
    return f'"order-{order.id}-v{order.version}"'


def _check_if_match(order):
    expected = request.headers.get("If-Match")
    if not expected:
        return problem(412, "precondition-failed", "If-Match is required for updates")
    if expected.strip() != _etag(order):
        return problem(412, "precondition-failed", "The supplied ETag is stale")
    return None


def _validate_create(body):
    errors = []
    if not isinstance(body.get("userId"), int): errors.append(["userId", "required integer"])
    if not isinstance(body.get("itemId"), int): errors.append(["itemId", "required integer"])
    if not isinstance(body.get("quantity"), int) or body.get("quantity") <= 0: errors.append(["quantity", "positive integer"])
    if not isinstance(body.get("amount"), int) or body.get("amount") <= 0: errors.append(["amount", "positive integer in paise"])
    if not body.get("cardToken"): errors.append(["cardToken", "required"])
    return errors


def _validate_update(body, patch=False):
    required = ["userId", "itemId", "quantity", "amount", "status"]
    errors = []
    if not patch:
        for field in required:
            if field not in body: errors.append([field, "required"])
    if "userId" in body and not isinstance(body["userId"], int): errors.append(["userId", "integer"])
    if "itemId" in body and not isinstance(body["itemId"], int): errors.append(["itemId", "integer"])
    if "quantity" in body and (not isinstance(body["quantity"], int) or body["quantity"] <= 0): errors.append(["quantity", "positive integer"])
    if "amount" in body and (not isinstance(body["amount"], int) or body["amount"] <= 0): errors.append(["amount", "positive integer"])
    if "status" in body and body["status"] not in ALLOWED_STATUSES: errors.append(["status", "unsupported status"])
    return errors


@app.before_request
def before_request():
    if request.method == "OPTIONS":
        return None
    ok, remaining = _rate_limit()
    request.rate_remaining = remaining
    if not ok:
        return problem(429, "too-many-requests", "Per-client request budget exceeded", {"Retry-After": "60"})


@app.after_request
def after_request(response):
    remaining = getattr(request, "rate_remaining", RATE_LIMIT)
    response.headers["X-RateLimit-Limit"] = str(RATE_LIMIT)
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    origin = request.headers.get("Origin")
    if origin:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
    else:
        response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept, Authorization, Idempotency-Key, If-Match, If-None-Match, X-HTTP-Method-Override"
    if response.status_code == 429:
        response.headers.setdefault("Retry-After", "60")
    if response.direct_passthrough or response.status_code in (204, 304):
        return response
    if response.get_data() and "Content-Type" not in response.headers:
        response.headers["Content-Type"] = "application/json"
    if request.headers.get("Accept-Encoding", "").lower().find("gzip") >= 0 and len(response.get_data()) > 1000 and response.status_code not in (204, 304):
        response.set_data(gzip.compress(response.get_data()))
        response.headers["Content-Encoding"] = "gzip"
        response.headers["Vary"] = "Accept-Encoding"
    return response


@app.route("/orders", methods=["OPTIONS"])
@app.route("/orders/<int:order_id>", methods=["OPTIONS"])
def options_orders(order_id=None):
    allow = "GET, POST, OPTIONS" if order_id is None else "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    return Response(status=204, headers={"Allow": allow})


@app.route("/orders", methods=["POST"])
def create_order():
    issue = _require_json()
    if issue: return issue
    body = request.get_json(silent=True)
    if not isinstance(body, dict): return problem(400, "invalid-request", "Malformed JSON body")
    errors = _validate_create(body)
    if errors: return problem(400, "invalid-request", str(errors))
    key = request.headers.get("Idempotency-Key")
    if key and key in _IDEMPOTENCY_RESULTS:
        saved = _IDEMPOTENCY_RESULTS[key]
        return jsonify(saved["body"]),200,saved["headers"]
    if key:
        previous = store.find_by_key(key)
        if previous:
            result = {"body": previous.as_json(),
                      "status": 200,
                      "headers": {"ETag": _etag(previous)}
                      }
            _IDEMPOTENCY_RESULTS[key] = result
            return jsonify(result["body"]), 200, result["headers"]
    order_id = store.reserve_id()
    payment_key = key or str(uuid.uuid4())
    try:
        payment = charge_with_retry(order_id, body["amount"], body["cardToken"], payment_key)
    except CardDeclined as exc:
        return problem(422, "payment-declined", str(exc))
    except PaymentsUnavailable:
        return problem(503, "payments-unavailable", "Payments service could not be reached")
    order = store.create(body["userId"], body["itemId"], body["quantity"], body["amount"], "confirmed", payment.get("id"), key, order_id=order_id)
    headers = {"Location": f"/orders/{order.id}", "ETag": _etag(order), "Cache-Control": "no-store"}
    result = {"body": order.as_json(), "status": 201, "headers": headers}
    if key: _IDEMPOTENCY_RESULTS[key] = result
    return jsonify(order.as_json()), 201, headers


@app.route("/orders", methods=["GET"])
@_bearer_required
def list_orders():
    issue = _require_json()
    if issue: return issue
    user_id = request.args.get("userId", type=int)
    status = request.args.get("status")
    sort = request.args.get("sort", "id")
    order = request.args.get("order", "asc")
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 20, type=int)
    if request.args.get("userId") is not None and user_id is None: return problem(400, "invalid-request", "userId must be an integer")
    if status is not None and status not in ALLOWED_STATUSES: return problem(400, "invalid-request", "unsupported status")
    if sort not in ALLOWED_SORTS or order not in {"asc", "desc"} or page < 1 or limit < 1 or limit > 100:
        return problem(400, "invalid-request", "invalid sort, order, page or limit")
    orders = store.find_by_filter(user_id, status, sort, order, page, limit)
    return jsonify([o.as_json() for o in orders]), 200


@app.route("/orders/<int:order_id>", methods=["GET"])
@_bearer_required
def get_order(order_id):
    issue = _require_json()
    if issue: return issue
    order = store.find(order_id)
    if order is None: return problem(404, "order-not-found", f"No order {order_id}")
    tag = _etag(order)
    if request.headers.get("If-None-Match", "").strip() == tag:
        return Response(status=304, headers={"ETag": tag, "Cache-Control": "private, max-age=60"})
    return jsonify(order.as_json()), 200, {"ETag": tag, "Cache-Control": "private, max-age=60"}


@app.route("/orders/<int:order_id>", methods=["POST"])
def method_override_order(order_id):
    override = request.headers.get("X-HTTP-Method-Override", "").upper()
    if override == "PUT":
        return put_order(order_id)
    if override == "PATCH":
        return patch_order(order_id)
    if override == "DELETE":
        return delete_order(order_id)
    return problem(405, "invalid-request", "POST to /orders/{id} is only a documented method-override fallback")


@app.route("/orders/<int:order_id>", methods=["PUT"])
@_bearer_required
def put_order(order_id):
    issue = _require_json()
    if issue: return issue
    order = store.find(order_id)
    if order is None: return problem(404, "order-not-found", f"No order {order_id}")
    pre = _check_if_match(order)
    if pre: return pre
    body = request.get_json(silent=True)
    if not isinstance(body, dict): return problem(400, "invalid-request", "Malformed JSON body")
    errors = _validate_update(body)
    if errors: return problem(400, "invalid-request", str(errors))
    updated = store.replace(order, body["userId"], body["itemId"], body["quantity"], body["amount"], body["status"])
    return jsonify(updated.as_json()), 200, {"ETag": _etag(updated)}


@app.route("/orders/<int:order_id>", methods=["PATCH"])
@_bearer_required
def patch_order(order_id):
    issue = _require_json()
    if issue: return issue
    order = store.find(order_id)
    if order is None: return problem(404, "order-not-found", f"No order {order_id}")
    pre = _check_if_match(order)
    if pre: return pre
    body = request.get_json(silent=True)
    if not isinstance(body, dict): return problem(400, "invalid-request", "Malformed JSON body")
    errors = _validate_update(body, patch=True)
    if errors or not body: return problem(400, "invalid-request", str(errors or [["body", "at least one field required"]]))
    updated = store.patch(order, body.get("quantity"), body.get("status"))
    return jsonify(updated.as_json()), 200, {"ETag": _etag(updated)}


@app.route("/orders/<int:order_id>", methods=["DELETE"])
@_bearer_required
def delete_order(order_id):
    order = store.find(order_id)
    if order is None: return problem(404, "order-not-found", f"No order {order_id}")
    # DELETE is idempotent. Removing the resource from the store makes a repeated delete return 404.
    store._orders.pop(order_id, None)
    return Response(status=204)


@app.route("/orders/<int:order_id>/cancellation", methods=["POST"])
@_bearer_required
def cancel_order(order_id):
    issue = _require_json()
    if issue: return issue
    order = store.find(order_id)
    if order is None: return problem(404, "order-not-found", f"No order {order_id}")
    key = request.headers.get("Idempotency-Key")
    cache_key = f"cancel:{order_id}:{key}" if key else None
    if cache_key and cache_key in _IDEMPOTENCY_RESULTS:
        saved = _IDEMPOTENCY_RESULTS[cache_key]
        return jsonify(saved["body"]), saved["status"]
    if order.status == "cancelled": return problem(409, "order-conflict", "Order is already cancelled")
    if order.status != "confirmed": return problem(409, "order-conflict", f"Order status is {order.status}")
    order.status = "cancelled"
    order.touch()
    body = {"orderId": order.id, "status": order.status}
    if cache_key: _IDEMPOTENCY_RESULTS[cache_key] = {"body": body, "status": 202, "headers": {}}
    return jsonify(body), 202



if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", "8090")))
