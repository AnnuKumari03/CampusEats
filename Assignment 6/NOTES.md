# CS543 — Assignment 6: Honest Responses, Status Codes, Errors & Validation

## Team details
- Group: 10
- Team leader: Annu Kumari
- Team member: Akanksha Upadhayay
- Team member: Prerna
- Roll numbers: **Add each member's roll number before submission.** Roll numbers were not present in the supplied repository files.

## Basis and scope
This submission is based on the supplied `CampusEats/LAb5.zip` Assignment 5 service. It is the same Flask Orders service (`app.py`, `models.py`, `store.py`, `payments_client.py`) on port 8090; no separate service was created. The existing A5 order body is `userId`, `itemId`, `quantity`, `amount` (paise), and `cardToken`. Its model stores one `itemId` and has no cart collection or delivery address. To avoid inventing a new CampusEats data model, this update retains that A5 payload. Therefore the generic brief's `items[]`/`address` example is not silently claimed as implemented; see the limitation note under Part C.

## Part A — Status codes

### A1. Status map (actual service routes)
- `POST /orders` — `201 Created` when a new order and payment are created; `200 OK` for a replay with the same `Idempotency-Key`; `400` for malformed JSON or wrong request Content-Type; `406` for an unsupported `Accept`; `422` for field validation or a declined payment; `429` for rate limiting; `503` for unavailable Payments dependency; `500` for unexpected server errors.
- `GET /orders` — `200 OK` with filtered orders; `400` for invalid query values; `401` for missing/empty bearer token; `406` for unsupported response format; `429` for rate limiting; `500` for unexpected errors.
- `GET /orders/{id}` — `200 OK` with the order; `304 Not Modified` when `If-None-Match` matches (no body); `401` for missing/empty bearer token; `404` for unknown order; `406` for unsupported format; `429` for rate limiting; `500` for unexpected errors.
- `PATCH /orders/{id}` — `200 OK` when updated; `400` for malformed JSON/wrong Content-Type; `401` for missing/empty bearer token; `404` for unknown order; `412` when `If-Match` is absent or stale; `422` for invalid fields; `409` for an illegal status transition; `406` for unsupported format; `429` for rate limiting; `500` for unexpected errors.
- `PUT /orders/{id}` — `200 OK` when replaced; `400` for malformed JSON/wrong Content-Type; `401` for missing/empty bearer token; `404` for unknown order; `412` when `If-Match` is absent or stale; `422` for invalid fields; `406` for unsupported format; `429` for rate limiting; `500` for unexpected errors.
- `DELETE /orders/{id}` — `204 No Content` when deleted; `401` for missing/empty bearer token; `404` if the order is missing; `406` for unsupported format; `429` for rate limiting; `500` for unexpected errors.
- Existing A5 extra route `POST /orders/{id}/cancellation` — `202 Accepted` when cancellation is accepted; `401`, `404`, `409` for an illegal cancellation transition, `406`, `429`, or `500` as applicable.
- `OPTIONS /orders` and `OPTIONS /orders/{id}` — `204 No Content`, with `Allow` advertising the supported methods.

The HTTP status communicates the result; failure responses are not returned as `200 {"ok": false}`. A newly created order has a `Location: /orders/{id}` header.

### A2. Responses that previously used 200 for failure
Validation failures on create/update are now `422` with a field-level `errors` array. Payment declines are `422`, missing orders are `404`, stale ETags are `412`, illegal status transitions are `409`, rate-limit failures are `429`, and unexpected exceptions are mapped to `500`.

### A3. Location
A successful new `POST /orders` returns `201 Created` and `Location: /orders/<id>`, for example `/orders/1`. The exact ID depends on the local run.

### A4. Retry safety
- `GET /orders` and `GET /orders/{id}` are safe to retry because they read state only. Conditional GET can return `304`.
- `POST /orders` is not inherently idempotent; the A5 `Idempotency-Key` returns the original result and prevents duplicate order/payment work when the same key is reused.
- `PUT` is intended to be idempotent at the representation level; `If-Match` prevents stale writes.
- `PATCH` depends on the change; this implementation requires `If-Match`, and status transitions are checked.
- `DELETE` leaves the resource deleted; a repeated delete may return `404`, which does not undo the first deletion.
- Retry transient `429` after `Retry-After: 60` and `503` after `Retry-After: 5`. Do not blindly retry an unchanged `4xx`; correct the request or resolve the precondition/conflict first.

## Part B — One error shape

### B1. Problem Details
All errors produced through `problem()` use `application/problem+json; charset=utf-8` and the fields `type`, `title`, `status`, and `detail`. Validation responses additionally contain `errors`.

### B2. Stable type catalogue
- `empty-cart` — requested cart has no items. **Not currently triggerable:** A5 stores one `itemId` per order and has no cart endpoint.
- `item-unavailable` — a menu item is unavailable. **Not currently triggerable:** the supplied A5 Orders service has no menu/availability store.
- `payment-declined` — Payments dependency returns a decline; client receives a clean message, not the upstream provider detail.
- `order-not-found` — requested order ID is absent.
- `illegal-transition` — requested order status/cancellation transition is not allowed.
- Supporting types: `invalid-request`, `validation-error`, `unauthorized`, `not-acceptable`, `precondition-failed`, `too-many-requests`, `payments-unavailable`, and `internal-error`.

The two unavailable domain cases are documented but are not fabricated as working features because the supplied A5 code has no cart or menu availability model.

### B3. Example Problem Details body
Example shape for an unknown order (ID depends on the local request):
```json
{
  "type": "https://api.campuseats.dev/problems/order-not-found",
  "title": "Order not found",
  "status": 404,
  "detail": "No order 999"
}
```
- `type`: stable problem URI.
- `title`: short human-readable label.
- `status`: same status as the HTTP response.
- `detail`: clean explanation, without a stack trace or database internals.

### B4. Two field-level errors in one 422
Example request omitting `userId` and using an invalid `quantity`:
```json
{
  "type": "https://api.campuseats.dev/problems/validation-error",
  "title": "Validation failed",
  "status": 422,
  "detail": "One or more fields are invalid.",
  "errors": [
    {"field": "userId", "message": "required integer"},
    {"field": "quantity", "message": "positive integer"}
  ]
}
```
The service collects all validation issues before returning one response.

### B5. Internal error mapping and hidden details
The global exception handler logs the exception server-side with `app.logger.exception(...)` and returns `500` with `internal-error` and a generic detail. It does not return the traceback or exception/database message. Payment declines are also mapped to a clean `payment-declined` detail instead of forwarding provider text. Payment dependency outages return `503` with a generic message and `Retry-After`.

## Part C — Request validation and formats

### C1–C2. Validation
The existing A5 request schema is retained: `userId` integer, `itemId` integer, `quantity` positive integer, `amount` positive integer in paise, and `cardToken` required. All these fields are checked before payment/order creation; validation issues are returned together as one `422` with `errors[]`.

**Compatibility limitation:** the generic Assignment 6 sheet describes `items` as a non-empty array and requires `address`. Those fields are not part of the supplied A5 CampusEats order model or request body. This submission deliberately does not claim to implement them or invent an address/cart data model. If the instructor requires those exact fields, the team should confirm whether the A5 contract is expected to change.

### C3. Content negotiation
`Accept: application/json` (or no Accept header) returns JSON. `Accept: application/xml` returns XML for order/list success responses. An unsupported format such as `application/pdf` returns `406 Not Acceptable`.

### C4. Content-Type
JSON bodies use UTF-8 content types; Problem Details uses `application/problem+json; charset=utf-8`; XML order bodies use `application/xml; charset=utf-8`. `204` and `304` have no response body.

## Part D — curl proof

See `transcript.txt` for commands to run against the local service. The archive supplied for A5 explicitly left actual `curl -v` capture sections as placeholders. No actual server transcript can be claimed until the service and Payments dependency are run locally. Replace the marked capture areas with the actual terminal output before submitting.

- Success: capture `201`, `Location`, JSON order body.
- Failures: validation `422`, unknown ID `404`, illegal transition `409`, rate limit `429` + `Retry-After`, payment decline `422`, Payments unavailable `503` + `Retry-After`.
- Negotiation: capture JSON and XML with their respective `Accept` headers.
- Regression: rerun the A5 idempotency and timeout/payment retry checks.

## Submission checklist
- [ ] Confirm roll numbers and add them above.
- [ ] Run `pip install -r requirements.txt`.
- [ ] Start the Payments dependency expected by A5, or configure `PAYMENTS_URL`.
- [ ] Run `flask --app app run --port 8090`.
- [ ] Run `pytest -q` and fix any local failures.
- [ ] Run every command in `transcript.txt` and replace capture placeholders with actual output.
- [ ] Validate `openapi.yaml` with `openapi-spec-validator openapi.yaml`.
- [ ] Submit this folder as one ZIP.
