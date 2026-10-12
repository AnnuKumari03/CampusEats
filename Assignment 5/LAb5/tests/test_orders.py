import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as application
import store

BODY = {"userId": 10, "itemId": 101, "quantity": 2, "amount": 50000, "cardToken": "tok_demo_12345"}
AUTH = {"Authorization": "Bearer demo-token"}


def fake_charge(*args, **kwargs):
    return {"id": 9001, "status": "captured"}


def setup_function():
    store.reset()
    application._RATE.clear()
    application._IDEMPOTENCY_RESULTS.clear()
    application.charge_with_retry = fake_charge


def create(client, key="order-1"):
    h = {**AUTH, "Idempotency-Key": key}
    return client.post("/orders", json=BODY, headers=h)


def test_create_location_etag_and_no_store():
    c = application.app.test_client()
    r = create(c)
    assert r.status_code == 201
    assert r.headers["Location"] == "/orders/1"
    assert r.headers["ETag"] == '"order-1-v1"'
    assert r.headers["Cache-Control"] == "no-store"


def test_idempotent_repeat():
    c = application.app.test_client()
    a, b = create(c), create(c)
    assert a.status_code == 201 and b.status_code == 200
    assert a.json == b.json


def test_get_and_304():
    c = application.app.test_client(); create(c)
    r = c.get("/orders/1", headers={**AUTH, "Accept": "application/json"})
    assert r.status_code == 200
    tag = r.headers["ETag"]
    r2 = c.get("/orders/1", headers={**AUTH, "If-None-Match": tag})
    assert r2.status_code == 304
    assert not r2.data


def test_put_stale_etag_412():
    c = application.app.test_client(); create(c)
    first = c.get("/orders/1", headers=AUTH)
    stale = first.headers["ETag"]
    c.put("/orders/1", json={"userId":10,"itemId":101,"quantity":3,"amount":50000,"status":"confirmed"}, headers={**AUTH, "If-Match": stale})
    r = c.put("/orders/1", json={"userId":10,"itemId":101,"quantity":4,"amount":50000,"status":"confirmed"}, headers={**AUTH, "If-Match": stale})
    assert r.status_code == 412


def test_bad_missing_fields_400():
    c = application.app.test_client()
    r = c.post("/orders", json={"userId":10}, headers=AUTH)
    assert r.status_code == 400


def test_unknown_404_and_auth_401():
    c = application.app.test_client()
    assert c.get("/orders/999", headers=AUTH).status_code == 404
    assert c.get("/orders/1", headers={"Authorization":"Bearer "}).status_code == 401


def test_accept_406():
    c = application.app.test_client(); create(c)
    r = c.get("/orders/1", headers={**AUTH, "Accept":"application/xml"})
    assert r.status_code == 406


def test_options_allow_and_cors():
    c = application.app.test_client()
    r = c.options("/orders")
    assert r.status_code == 204
    assert r.headers["Allow"] == "GET, POST, OPTIONS"
    r = c.options("/orders", headers={"Origin":"https://frontend.example", "Access-Control-Request-Method":"POST"})
    assert r.headers["Access-Control-Allow-Origin"] == "https://frontend.example"


def test_list_query_sort_pagination():
    c = application.app.test_client()
    create(c, "one"); create(c, "two")
    r = c.get("/orders?userId=10&status=confirmed&sort=createdAt&order=desc&page=1&limit=1", headers=AUTH)
    assert r.status_code == 200
    assert len(r.json) == 1


def test_patch_and_delete():
    c = application.app.test_client(); create(c)
    tag = c.get("/orders/1", headers=AUTH).headers["ETag"]
    r = c.patch("/orders/1", json={"quantity":3}, headers={**AUTH, "If-Match":tag})
    assert r.status_code == 200
    r = c.delete("/orders/1", headers=AUTH)
    assert r.status_code == 204
