# CampusEats — Assignment 5 Submission

This folder contains the CampusEats Assignment 5 update of the Orders service.

## Contents

- `app.py` — REST endpoints, HTTP methods, headers, CORS, rate limiting, ETag/conditional requests, idempotency and method-override fallback.
- `models.py` — Order model with representation versioning for ETags.
- `store.py` — in-memory order storage, filtering/sorting/pagination and update operations.
- `payments_client.py` — payment dependency client with timeout/retry behavior.
- `errors.py` — consistent JSON problem responses.
- `openapi.yaml` — Assignment 5 OpenAPI contract.
- `tests/test_orders.py` — Assignment 5 tests.
- `NOTES.md` — method map, headers table, safe-retry plan and all eight required answers.
- `curl-transcript.txt` — Mac/Linux curl -v verification command set for the required HTTP exchanges; run these commands locally and replace the marked capture sections with the terminal output before final submission.
- `requirements.txt` — Python dependencies.

## Run

```bash
pip install -r requirements.txt
flask --app app run --port 8090
```

The Payments dependency is configured with `PAYMENTS_URL`; the default is `http://localhost:8080`. Start the Assignment 4 payment service (or configure a compatible payment service) before running the create transcript.

## Validate

```bash
python -m py_compile *.py tests/test_orders.py
pytest -q
openapi-spec-validator openapi.yaml
```

For the final instructor verification, run the service locally and capture the commands in `curl-transcript.txt` with `curl -v` so the file contains the actual request/response transcript from the student's environment.
