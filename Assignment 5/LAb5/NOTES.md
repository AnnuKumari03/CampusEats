# CS543 Web Services — Assignment 5: HTTP Methods & Headers

**Team ID:** 10  
**Team Leader:** Annu Kumari — 20251651024  
**Team Member:** Prerna — 20251651072  
**Team Member:** Akanksha Upadhaya — 20251651011

## Part A — Methods & the message

### A1. CampusEats method map

| Action | Method | URL |
|---|---|---|
| Create order | POST | `/orders` |
| List/filter/sort/page orders | GET | `/orders?userId=10&status=confirmed&sort=createdAt&order=desc&page=1&limit=20` |
| Read one order | GET | `/orders/{id}` |
| Replace an order | PUT | `/orders/{id}` |
| Partially modify an order | PATCH | `/orders/{id}` |
| Delete an order | DELETE | `/orders/{id}` |
| Cancel an order | POST | `/orders/{id}/cancellation` |
| Discover allowed methods | OPTIONS | `/orders` or `/orders/{id}` |

The resource noun is `orders`; the HTTP method expresses the operation. No action is put into a verb URL such as `/cancelOrder`.

### A2. Non-CRUD action

Cancellation is not ordinary CRUD. It is represented as:

`POST /orders/{id}/cancellation`

This follows the required sub-resource pattern and keeps the action out of the URL as a verb.

### A3. Safe and idempotent

| Endpoint | Safe? | Idempotent? | Retry note |
|---|---|---|---|
| GET `/orders` | Yes | Yes | Naturally retry-safe |
| GET `/orders/{id}` | Yes | Yes | Naturally retry-safe; `If-None-Match` avoids re-downloading unchanged data |
| POST `/orders` | No | No by default | `Idempotency-Key` prevents duplicate order/payment work |
| PUT `/orders/{id}` | No | Yes | `If-Match` prevents stale writes |
| PATCH `/orders/{id}` | No | Depends on operation | `If-Match` prevents stale writes |
| DELETE `/orders/{id}` | No | Yes | Repeating the request leaves the resource deleted; a later 404 is acceptable |
| POST `/orders/{id}/cancellation` | No | Not assumed | `Idempotency-Key` prevents duplicate cancellation processing |

GET never changes server state.

### A4. Query parameters

The list endpoint is a pure GET. Example:

`GET /orders?userId=10&status=confirmed&sort=createdAt&order=desc&page=1&limit=20`

Filtering, sorting and pagination are represented in the query string. A POST search would only be justified for unusually large or complex structured search criteria that do not fit conveniently in a URL.

### A5. OPTIONS, Allow and method override

`OPTIONS /orders` returns:

`Allow: GET, POST, OPTIONS`

`OPTIONS /orders/{id}` returns:

`Allow: GET, POST, PUT, PATCH, DELETE, OPTIONS`

For constrained clients that cannot send PUT/PATCH/DELETE, the documented fallback is `X-HTTP-Method-Override` on a POST transport request. It is a fallback only; normal clients use the actual HTTP method.

### A6. Complete HTTP exchange

**Request — HTTP/1.1**

```http
POST /orders HTTP/1.1
Host: localhost:8090
Content-Type: application/json
Accept: application/json
Idempotency-Key: order-001

{"userId":10,"itemId":101,"quantity":2,"amount":50000,"cardToken":"tok_demo_12345"}
```

**Response**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /orders/1
ETag: "order-1-v1"
Cache-Control: no-store
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains

{"id":1,"userId":10,"itemId":101,"quantity":2,"amount":50000,"status":"confirmed","paymentId":9001,"createdAt":"..."}
```

## Part B — Headers on every message

### B1. Content-Type and negotiation

JSON request bodies use `Content-Type: application/json`. Clients request JSON with `Accept: application/json`. If a client requests an unsupported representation such as `application/xml`, the service returns `406 Not Acceptable`.

For large JSON responses, the service supports gzip when the client advertises `Accept-Encoding: gzip`; the response then includes `Content-Encoding: gzip`.

### B2. Status codes and Location

- `201 Created` + `Location` — new order created.
- `200 OK` — successful read/list/update or idempotent repeat.
- `202 Accepted` — cancellation accepted.
- `204 No Content` — successful DELETE and OPTIONS.
- `400 Bad Request` — malformed JSON, invalid fields or invalid query parameters.
- `401 Unauthorized` — missing/empty bearer token on protected endpoints.
- `404 Not Found` — missing order.
- `409 Conflict` — cancellation not allowed by current order state.
- `412 Precondition Failed` — stale/missing `If-Match` for update.
- `422 Unprocessable Entity` — valid order rejected by a domain rule such as payment decline.
- `429 Too Many Requests` — per-client rate budget exceeded.
- `503 Service Unavailable` — Payments dependency unavailable.

`Location` on `201` points to the newly created order. On a `3xx` response, `Location` would point to the redirect target.

### B3. Authorization

Protected endpoints accept:

`Authorization: Bearer <token>`

No real token validation system is required for this assignment. A missing or empty bearer token returns `401 Unauthorized`.

### B4. Cache-Control and ETag

A single-order GET returns an ETag such as:

`ETag: "order-1-v1"`

The ETag changes whenever the order representation is changed. Cacheable single-item reads use:

`Cache-Control: private, max-age=60`

Order creation uses `Cache-Control: no-store` because its response is user-specific and includes payment-related information.

### B5. Rate limiting

Every normal response includes:

`X-RateLimit-Limit: 60`

`X-RateLimit-Remaining: <remaining>`

The budget is tracked per client. When the budget is exceeded the service returns `429 Too Many Requests` with:

`Retry-After: 60`

### B6. CORS

The service returns `Access-Control-Allow-Origin` and handles OPTIONS preflight requests. It also advertises:

`Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS`

and the supported request headers:

`Access-Control-Allow-Headers: Content-Type, Accept, Authorization, Idempotency-Key, If-Match, If-None-Match, X-HTTP-Method-Override`

### B7. Security and general headers

The service adds:

`X-Content-Type-Options: nosniff`

`Strict-Transport-Security: max-age=31536000; includeSubDomains`

The framework supplies normal HTTP metadata such as `Date` and `Server` when deployed. HTTPS is required in production.

## Part C — Caching & safe retries

### C1. Conditional GET → 304

A normal read returns:

`ETag: "order-1-v1"`

The client can later send:

`If-None-Match: "order-1-v1"`

If the representation is unchanged, the service returns `304 Not Modified` with no response body. This avoids transferring the unchanged JSON representation again.

### C2. Conditional write → 412

An update sends:

`If-Match: "order-1-v1"`

If the current order has a newer ETag, the service returns `412 Precondition Failed`. This prevents one editor from overwriting a newer representation.

### C3. Idempotency-Key

Order creation uses:

`Idempotency-Key: order-001`

A repeated create with the same key returns the original result and does not repeat the payment/order creation work. This matters because duplicate processing could charge the customer twice and create two CampusEats orders.

Cancellation also accepts an idempotency key so a retried cancellation does not repeat the action processing.

### C4. Safe-retry plan

| Endpoint | Mechanism | Why |
|---|---|---|
| GET `/orders` | Natural HTTP idempotency | Safe read; retry does not create state changes |
| GET `/orders/{id}` | `If-None-Match` | Avoids downloading unchanged data on retry |
| POST `/orders` | `Idempotency-Key` | Prevents duplicate order/payment work |
| PUT `/orders/{id}` | `If-Match` | Prevents stale representation from overwriting newer data |
| PATCH `/orders/{id}` | `If-Match` | Prevents lost updates |
| DELETE `/orders/{id}` | HTTP idempotency | Final state remains deleted |
| POST `/orders/{id}/cancellation` | `Idempotency-Key` | Prevents duplicate action processing |

## Part D — Verify & document

### D1. curl -v transcript

The supplied `curl-transcript.txt` contains the Mac/Linux `curl -v` commands and the required HTTP exchanges to capture for:

1. Successful create — 201 + Location.
2. Same create with the same Idempotency-Key — original result.
3. Conditional GET — 304.
4. Conditional write with stale ETag — 412.
5. 400 malformed input.
6. 404 missing order.
7. 401 empty bearer token.
8. OPTIONS + Allow.
9. 406 unsupported Accept.
10. 429 rate-limit exhaustion.
11. CORS preflight.

### D2. Headers table

| Endpoint | Request headers needed | Response headers set |
|---|---|---|
| POST `/orders` | Content-Type, Accept, Idempotency-Key | Content-Type, Location, ETag, Cache-Control, rate-limit, security, CORS |
| GET `/orders` | Accept, Authorization | Content-Type, rate-limit, security, CORS |
| GET `/orders/{id}` | Accept, Authorization, If-None-Match | Content-Type, ETag, Cache-Control, rate-limit, security, CORS |
| PUT `/orders/{id}` | Content-Type, Accept, Authorization, If-Match | Content-Type, ETag, rate-limit, security, CORS |
| PATCH `/orders/{id}` | Content-Type, Accept, Authorization, If-Match | Content-Type, ETag, rate-limit, security, CORS |
| DELETE `/orders/{id}` | Authorization | rate-limit, security, CORS |
| POST `/orders/{id}/cancellation` | Accept, Authorization, Idempotency-Key | Content-Type, rate-limit, security, CORS |
| OPTIONS `/orders` | Origin, Access-Control-Request-Method, Access-Control-Request-Headers | Allow, CORS headers |

## Required eight answers

### 1. Three endpoints: method, success status, most important response header

**POST `/orders`** — `201 Created`; `Location` matters most because it identifies the newly created resource.

**GET `/orders/{id}`** — `200 OK`; `ETag` matters most because it supports cache validation and conditional requests.

**PUT `/orders/{id}`** — `200 OK`; `ETag` matters most because the updated representation must be identifiable for later `If-Match` checks.

### 2. Safe and idempotent endpoints

GET endpoints are safe and idempotent. PUT and DELETE are not safe but are idempotent when implemented normally. POST `/orders` is neither safe nor naturally idempotent, so `Idempotency-Key` makes retries safe from duplicate creation. Cancellation is also a POST action and is not assumed idempotent; its idempotency key prevents duplicate processing.

### 3. ETag, 304 and 412

Example:

`ETag: "order-1-v1"`

304 request:

`If-None-Match: "order-1-v1"`

An unchanged resource returns `304 Not Modified`, which saves the response body transfer.

412 request:

`If-Match: "order-1-v1"`

If the current ETag differs, the service returns `412 Precondition Failed`, preventing an older editor from overwriting a newer version.

### 4. 422 versus 400

A malformed create request such as:

```http
POST /orders
Content-Type: application/json

{"userId":10,"quantity":-2}
```

returns `400 Bad Request` because required fields are missing/invalid.

A structurally valid request whose payment provider declines the payment returns `422 Unprocessable Entity` because the request is syntactically valid but rejected by a domain rule.

### 5. Browser blocked despite server 200

The browser's same-origin/CORS enforcement blocks the response from being exposed to the web page. The response needs the appropriate `Access-Control-Allow-Origin` header, and the server must answer the OPTIONS preflight when required.

### 6. Cacheable and no-store responses

A single-order GET can use:

`Cache-Control: private, max-age=60`

because the representation can be revalidated with its ETag.

An order-creation response uses:

`Cache-Control: no-store`

because it is user-specific and contains payment-related information that should not be stored by caches.

### 7. When POST is appropriate for search

POST can be appropriate when a search is too complex or large to represent conveniently in a GET query string, for example a large structured filter body. Switching from GET to POST gives up the normal benefits of GET such as simple URL bookmarking/sharing and conventional cacheability of a read request.

### 8. Meaning of Location on 201 and 3xx

On `201 Created`, `Location` points to the newly created resource, for example:

`Location: /orders/1`

On a `3xx` redirect, `Location` identifies the URI to which the client should redirect.

## Final submission checklist

- `openapi.yaml` updated with methods, statuses, headers and conditional requests.
- Updated source files and tests.
- `curl-transcript.txt` with required curl commands/exchanges.
- `NOTES.md` with method map, headers table, safe-retry plan and all eight answers.
- Team ID and all member roll numbers/names included.
- One ZIP submitted by the Team Leader.
