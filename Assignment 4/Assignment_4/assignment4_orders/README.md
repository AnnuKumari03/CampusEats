# CS543 Assignment 4 — CampusEats Orders

This is the completed Assignment 4 implementation based on the supplied CS543 Tutorial 4 material and the Orders-service requirements represented in this project.

## Run

```bash
pip install -r requirements.txt
openapi-spec-validator openapi.yaml
flask --app app run --port 8090
```

Set `PAYMENTS_URL` to the running Tutorial 4 Payments service before creating an order.

Run tests:

```bash
pytest -q
```
