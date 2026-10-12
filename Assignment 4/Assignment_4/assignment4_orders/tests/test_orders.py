import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as application
import store

BODY = {
    "userId": 10,
    "itemId": 101,
    "quantity": 2,
    "amount": 50000,
    "cardToken": "tok_demo_12345",
}

class FakePayment:
    def __init__(self, payment_id=9001):
        self.payment_id = payment_id

def fake_charge(*args, **kwargs):
    return {"id": 9001, "status": "captured"}

def setup_function():
    store.reset()
    application.charge_with_retry = fake_charge

def test_create_succeeds_with_location(client=None):
    client = application.app.test_client()
    response = client.post("/orders", json=BODY, headers={"Idempotency-Key": "order-1"})
    assert response.status_code == 201
    assert response.headers["Location"] == "/orders/1"

def test_same_key_returns_original(client=None):
    client = application.app.test_client()
    headers = {"Idempotency-Key": "order-1"}
    first = client.post("/orders", json=BODY, headers=headers)
    second = client.post("/orders", json=BODY, headers=headers)
    assert (first.status_code, second.status_code) == (201, 200)
    assert first.json["id"] == second.json["id"]

def test_bad_body_is_400(client=None):
    client = application.app.test_client()
    response = client.post("/orders", json={"userId": 10})
    assert response.status_code == 400
    assert set(response.json) == {"type", "title", "status", "detail"}

def test_unknown_order_is_404(client=None):
    client = application.app.test_client()
    assert client.get("/orders/999").status_code == 404


def test_cancel_confirmed_order():
    client = application.app.test_client()
    response = client.post("/orders", json=BODY, headers={"Idempotency-Key": "cancel-1"})
    assert response.status_code == 201
    order_id = response.json["id"]
    cancelled = client.post(f"/orders/{order_id}/cancellation")
    assert cancelled.status_code == 202
    assert cancelled.json["status"] == "cancelled"
    again = client.post(f"/orders/{order_id}/cancellation")
    assert again.status_code == 409

def test_list_orders_filters():
    client = application.app.test_client()
    client.post("/orders", json=BODY, headers={"Idempotency-Key": "list-1"})
    response = client.get("/orders?userId=10&status=confirmed")
    assert response.status_code == 200
    assert len(response.json) == 1

def test_invalid_filter_is_400():
    client = application.app.test_client()
    response = client.get("/orders?status=shipped")
    assert response.status_code == 400
