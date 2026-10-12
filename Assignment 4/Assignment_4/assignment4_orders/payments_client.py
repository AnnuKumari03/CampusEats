import os
import time
import random
import requests

PAYMENTS_URL = os.environ.get("PAYMENTS_URL", "http://localhost:8080")

class CardDeclined(Exception):
    pass

class PaymentsUnavailable(Exception):
    pass

def _post_payment(order_id, amount, card_token, key):
    response = requests.post(
        f"{PAYMENTS_URL}/payments",
        json={
            "orderId": order_id,
            "cardToken": card_token,
            "amount": amount,
            "currency": "INR",
        },
        headers={"Idempotency-Key": key},
        timeout=2.0,
    )
    if response.status_code in (200, 201):
        return response.json()
    if response.status_code == 422:
        data = response.json()
        raise CardDeclined(data.get("detail", "Payment was declined."))
    if response.status_code >= 500:
        raise PaymentsUnavailable()
    response.raise_for_status()

def charge_with_retry(order_id, amount, card_token, key):
    for attempt in range(3):
        try:
            return _post_payment(order_id, amount, card_token, key)
        except CardDeclined:
            raise
        except (PaymentsUnavailable, requests.exceptions.RequestException):
            if attempt == 2:
                raise PaymentsUnavailable("Payments service unavailable after 3 attempts")
            wait = (2 ** attempt) + random.random()
            time.sleep(wait)
