from flask import Flask, request, jsonify
import uuid
import store
from errors import problem
from payments_client import charge_with_retry, CardDeclined, PaymentsUnavailable

app = Flask(__name__)
ALLOWED_STATUSES = {"pending", "confirmed", "cancelled"}

def validate(body):
    errors = []
    if not isinstance(body.get("userId"), int):
        errors.append(["userId", "required integer"])
    if not isinstance(body.get("itemId"), int):
        errors.append(["itemId", "required integer"])
    if not isinstance(body.get("quantity"), int) or body.get("quantity") <= 0:
        errors.append(["quantity", "positive integer"])
    if not isinstance(body.get("amount"), int) or body.get("amount") <= 0:
        errors.append(["amount", "positive integer in paise"])
    if not body.get("cardToken"):
        errors.append(["cardToken", "required"])
    return errors

@app.post("/orders")
def create_order():
    body = request.get_json(silent=True) or {}
    errors = validate(body)
    if errors:
        return problem(400, "invalid-request", str(errors))

    key = request.headers.get("Idempotency-Key")
    if key:
        previous = store.find_by_key(key)
        if previous:
            return jsonify(previous.as_json()), 200

    order_id = store.reserve_id()
    payment_key = key or str(uuid.uuid4())

    try:
        payment = charge_with_retry(
            order_id, body["amount"], body["cardToken"], payment_key
        )
    except CardDeclined as exc:
        return problem(422, "payment-declined", str(exc))
    except PaymentsUnavailable:
        return problem(503, "payments-unavailable", "Payments service could not be reached")

    order = store.create(
        body["userId"], body["itemId"], body["quantity"], body["amount"],
        "confirmed", payment.get("id"), key, order_id=order_id
    )
    return jsonify(order.as_json()), 201, {"Location": f"/orders/{order.id}"}

@app.get("/orders/<int:order_id>")
def get_order(order_id):
    order = store.find(order_id)
    if order is None:
        return problem(404, "order-not-found", f"No order {order_id}")
    return jsonify(order.as_json()), 200

@app.get("/orders")
def list_orders():
    user_id = request.args.get("userId", type=int)
    status = request.args.get("status")
    if request.args.get("userId") is not None and user_id is None:
        return problem(400, "invalid-request", "userId must be an integer")
    if status is not None and status not in ALLOWED_STATUSES:
        return problem(400, "invalid-request", "unsupported status")
    orders = store.find_by_filter(user_id, status)
    return jsonify([o.as_json() for o in orders]), 200

@app.post("/orders/<int:order_id>/cancellation")
def cancel_order(order_id):
    order = store.find(order_id)
    if order is None:
        return problem(404, "order-not-found", f"No order {order_id}")
    if order.status == "cancelled":
        return problem(409, "order-conflict", "Order is already cancelled")
    if order.status != "confirmed":
        return problem(409, "order-conflict", f"Order status is {order.status}")
    order.status = "cancelled"
    return jsonify({"orderId": order.id, "status": order.status}), 202
