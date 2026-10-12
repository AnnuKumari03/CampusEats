from flask import jsonify

TITLES = {
    "invalid-request": "Invalid request",
    "order-not-found": "Order not found",
    "order-conflict": "Order state conflict",
    "payment-declined": "Payment declined",
    "payments-unavailable": "Payments service unavailable",
    "unauthorized": "Unauthorized",
    "not-acceptable": "Not acceptable",
    "precondition-failed": "Precondition failed",
    "too-many-requests": "Too many requests",
}

def problem(status, code, detail="", headers=None):
    body = {
        "type": f"/errors/{code}",
        "title": TITLES.get(code, "HTTP error"),
        "status": status,
        "detail": detail,
    }
    return jsonify(body), status, headers or {}
