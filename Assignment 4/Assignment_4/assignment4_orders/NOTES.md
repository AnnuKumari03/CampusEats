# Assignment 4 — CampusEats Orders REST Service

**Team ID:** 10  
**Team Leader:** Annu Kumari — 20251651024  
**Team Member:** Prerna — 20251651072  
**Team Member:** Akanksha Upadhaya — 20251651011

## Part A — Model the service

### A1. Selected service

**Orders**. The Orders service is used because an order is a durable CampusEats resource and it naturally needs to call the Payments service when an order is created. The service keeps ownership of order records in its own store.

### A2. SOAP-style operations from the earlier design

- createOrder(userId, itemId, quantity, amount, cardToken)
- getOrder(orderId)
- listOrders(userId, status)
- cancelOrder(orderId)

### A3. Resource nouns

- createOrder → orders
- getOrder → orders
- listOrders → orders
- cancelOrder → orders/cancellation

The verbs are removed from the URL. The URLs identify resources, while HTTP methods express the operation.

### A4. Resource table

| Method | URL | What it does | Success | Failure |
|---|---|---|---|---|
| POST | `/orders` | Creates an order and obtains payment confirmation | 201 | 400, 422, 503 |
| GET | `/orders/{id}` | Reads one order | 200 | 404 |
| GET | `/orders?userId=10&status=confirmed` | Lists orders using query filters | 200 | 400 |
| POST | `/orders/{id}/cancellation` | Starts cancellation of a confirmed order | 202 | 404, 409 |

### A5. Hard mapping choice

The least comfortable operation is `cancelOrder`, because “cancel” is an action rather than a durable noun. I mapped it to the `cancellation` sub-resource: `/orders/{id}/cancellation`. I rejected `GET /orders/{id}?do=cancel` because the Tutorial 4 guidance treats actions as sub-resources with an appropriate method. I also rejected `POST /cancelOrder` because verbs should not be used as resource paths.

## Part B — OpenAPI contract

The OpenAPI contract is written before the handler code. It contains `info`, `servers`, `paths`, and reusable `components.schemas`. Request and response shapes are referenced using `$ref` rather than copied inline.

Validate it with:

```bash
pip install -r requirements.txt
openapi-spec-validator openapi.yaml
```

Expected result:

```text
openapi.yaml: OK
```

## Part C — Implementation

The service follows the Tutorial 4 structure:

```text
orders/
├── openapi.yaml
├── models.py
├── store.py
├── errors.py
├── payments_client.py
├── app.py
├── requirements.txt
├── NOTES.md
└── tests/
    └── test_orders.py
```

`models.py` stores the complete `Order` record, including the idempotency key and internal payment information. `as_json()` publishes only the API representation. The idempotency key is not exposed in the response.

The `validate()` function performs the request validation before the body fields are used. Without it, malformed values such as a missing `amount`, non-integer `quantity`, or missing `cardToken` could cause an exception or an invalid order to reach the payment call.

The service uses these status codes:

- **201** — new order created, with `Location` header
- **200** — successful read or idempotent repeat
- **202** — cancellation accepted
- **400** — malformed request/filter
- **404** — unknown order
- **409** — order state does not permit cancellation
- **422** — payment provider declined a valid request
- **503** — Payments service is unavailable

All failures use the same `problem()` response shape:

```json
{
  "type": "/errors/order-not-found",
  "title": "Order not found",
  "status": 404,
  "detail": "No order 999"
}
```

## Part D — Network hardening

The Orders service calls the Payments service through `payments_client.py`. Its URL is read from the `PAYMENTS_URL` environment variable; it is not hard-coded into the business logic. The Tutorial 4 Payments service accepts `Idempotency-Key`, so the same key is used for all retry attempts of one order-creation intent.

The outbound request has a **2-second timeout**. It retries transport/service failures up to three times with exponential backoff and jitter. A 4xx response is not retried. A 422 card decline is treated as a business outcome and is returned as 422 immediately.

### Fallback when Payments is unreachable

The Orders service fails the order creation with **503 Service Unavailable** when Payments cannot be reached after the retry attempts. It does not create an order without payment confirmation because doing so could leave an order in the system whose payment status is unknown. A degraded “create anyway” fallback would therefore create an inconsistent order/payment state.

## Assignment 3 comparison

Assignment 4 changes the CampusEats service design from a SOAP-style operation model to REST resources. The supplied Tutorial 4 explains that OpenAPI replaces the WSDL contract for the REST service, HTTP status codes replace SOAP fault signalling, and service discovery can use a resolvable service name instead of a registry lookup.

### 1. WSDL and OpenAPI

The Assignment 4 `openapi.yaml` contains **199 lines** in the submitted file. It documents four Orders endpoints, reusable request/response schemas, query/path parameters, the `Idempotency-Key` header, and HTTP status codes. Tutorial 4 notes that the explicit SOAP **binding** and **service/port** structures are not needed in the REST contract because HTTP methods and URLs already provide that information. fileciteturn0file0L88-L98

> **Note:** The Assignment 3 `partner.wsdl` file is not included in the supplied Assignment 4 ZIP, so its exact line count should not be claimed here unless the original Assignment 3 file is also submitted/available.

### 2. SOAP Fault replaced by HTTP status + problem body

In this REST implementation, a valid order request whose payment is declined is returned as **422 Unprocessable Entity** with the common problem-response structure. Invalid input uses **400**, while an unavailable Payments service uses **503**. Tutorial 4 explicitly maps invalid requests to 400, card declines to 422, and gateway failure to 503. fileciteturn0file0L156-L185

This is preferable to returning an application failure inside HTTP 200 because the HTTP status communicates the outcome directly to clients and infrastructure.

### 3. UDDI: publish, find, bind

The REST deployment still needs the service to be deployed and discoverable, and the Orders service still resolves the Payments service name. A separate UDDI **bind** step disappears: the deployment platform/DNS resolves the service name and the client uses HTTP directly. Tutorial 4 gives `PAYMENTS_URL=http://payments:8080` as the example and explains the publish/find/bind transition. fileciteturn0file0L473-L498

### 4. XML Schema responsibility

In Assignment 3, XML Schema defined the SOAP message fields. In Assignment 4, the `validate()` function in `app.py` performs the equivalent application-level validation for the JSON request: required integer fields, positive quantity and amount, and the card token are checked before the payment call. This follows the Tutorial 4 principle of validating the request before indexing its fields. fileciteturn0file0L281-L300

### 5. Where SOAP would still be preferred

SOAP can still be appropriate at an external integration boundary when a partner requires a formally governed WSDL/XSD contract and SOAP-specific interoperability requirements. For this Assignment 4 implementation, however, the internal CampusEats Orders service is modelled as REST and communicates with the Tutorial 4 Payments REST service.

## Conclusion

Assignment 4 converts the service design from a SOAP-style operation model into REST resources, documents the contract with OpenAPI, implements four endpoints, uses one consistent error representation, makes order creation idempotent, and protects the Payments dependency with timeout, retry, backoff and jitter. The service keeps order data private to its own store and uses the HTTP status code to communicate the outcome to callers.
