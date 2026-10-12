from flask import jsonify

TITLES = {
    "invalid-request": "Invalid request",
    "order-not-found": "Order not found",
    "order-conflict": "Order state conflict",
    "payment-declined": "Payment declined",
    "payments-unavailable": "Payments service unavailable",
}

def problem(status, code, detail=""):
    body = {
        "type": f"/errors/{code}",
        "title": TITLES[code],
        "status": status,
        "detail": detail,
    }
    return jsonify(body), status
