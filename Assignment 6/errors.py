from flask import Response, jsonify
import json

TITLES = {
    "invalid-request": "Invalid request",
    "validation-error": "Validation failed",
    "empty-cart": "Empty cart",
    "item-unavailable": "Item unavailable",
    "payment-declined": "Payment declined",
    "order-not-found": "Order not found",
    "illegal-transition": "Illegal order transition",
    "order-conflict": "Order state conflict",
    "payments-unavailable": "Payments service unavailable",
    "unauthorized": "Unauthorized",
    "not-acceptable": "Not acceptable",
    "precondition-failed": "Precondition failed",
    "too-many-requests": "Too many requests",
    "internal-error": "Internal server error",
}

def problem(status, code, detail="", headers=None, errors=None):
    body = {
        "type": f"https://api.campuseats.dev/problems/{code}",
        "title": TITLES.get(code, "HTTP error"),
        "status": status,
        "detail": detail,
    }
    if errors is not None:
        body["errors"] = [{"field": field, "message": message} for field, message in errors]
    response = jsonify(body)
    response.status_code = status
    response.headers["Content-Type"] = "application/problem+json; charset=utf-8"
    for name, value in (headers or {}).items():
        response.headers[name] = value
    return response
