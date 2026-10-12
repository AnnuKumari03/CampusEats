# CampusEats — Assignment 6

This folder extends the supplied A5 Flask Orders service; it does not create a second service.

## Files
- `app.py` — Orders endpoints, Problem Details routing, validation, status-transition checks, Retry-After and JSON/XML negotiation.
- `errors.py` — shared `problem()` helper and stable problem titles.
- `models.py`, `store.py`, `payments_client.py` — preserved A5 service model/store/payment integration.
- `openapi.yaml` — API contract and Problem Details schema.
- `tests/test_orders.py` — A5 regression tests plus Assignment 6 checks.
- `transcript.txt` — curl commands with places to paste real local outputs.
- `NOTES.md` — ordered answers to Assignment 6.

## Run
```bash
pip install -r requirements.txt
flask --app app run --port 8090
```
The create-order route calls the Payments service from A5. Start that service or configure `PAYMENTS_URL` before testing a successful create.

## Verify
```bash
python -m py_compile app.py errors.py models.py store.py payments_client.py tests/test_orders.py
pytest -q
openapi-spec-validator openapi.yaml
```

## Important source-based note
The supplied A5 CampusEats service accepts `userId`, `itemId`, `quantity`, `amount`, and `cardToken`; it has no `items[]` cart or address field. `NOTES.md` documents this mismatch rather than pretending those fields exist. Actual curl output must be captured locally before final submission.
