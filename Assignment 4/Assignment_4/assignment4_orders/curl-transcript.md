# Curl transcript — Assignment 4

Set the dependency before starting the Orders service:

```bash
set PAYMENTS_URL=http://localhost:8080
flask --app app run --port 8090
```

## 1. Successful create

```bash
curl -i -X POST localhost:8090/orders ^
  -H "Content-Type: application/json" ^
  -H "Idempotency-Key: order-001" ^
  -d "{\"userId\":10,\"itemId\":101,\"quantity\":2,\"amount\":50000,\"cardToken\":\"tok_demo_12345\"}"
```

Expected:

```text
HTTP/1.1 201 CREATED
Location: /orders/1
Content-Type: application/json

{"id":1,"userId":10,"itemId":101,"quantity":2,"amount":50000,"status":"confirmed","paymentId":1,"createdAt":"..."}
```

## 2. Same request with the same idempotency key

Run the exact command again.

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"id":1,"userId":10,"itemId":101,"quantity":2,"amount":50000,"status":"confirmed","paymentId":1,"createdAt":"..."}
```

No second order is created and the payment call is not repeated from the Orders handler.

## 3. Malformed body

```bash
curl -i -X POST localhost:8090/orders ^
  -H "Content-Type: application/json" ^
  -d "{\"userId\":10,\"quantity\":-2}"
```

Expected:

```text
HTTP/1.1 400 BAD REQUEST
Content-Type: application/json

{"type":"/errors/invalid-request","title":"Invalid request","status":400,"detail":"..."}
```

## 4. Missing resource

```bash
curl -i localhost:8090/orders/999
```

Expected:

```text
HTTP/1.1 404 NOT FOUND
Content-Type: application/json

{"type":"/errors/order-not-found","title":"Order not found","status":404,"detail":"No order 999"}
```

## 5. State conflict

First cancel order 1:

```bash
curl -i -X POST localhost:8090/orders/1/cancellation
```

Expected:

```text
HTTP/1.1 202 ACCEPTED

{"orderId":1,"status":"cancelled"}
```

Then cancel it again:

```bash
curl -i -X POST localhost:8090/orders/1/cancellation
```

Expected:

```text
HTTP/1.1 409 CONFLICT
Content-Type: application/json

{"type":"/errors/order-conflict","title":"Order state conflict","status":409,"detail":"Order is already cancelled"}
```

## 6. Filtered list

```bash
curl -i "localhost:8090/orders?userId=10&status=confirmed"
```

Expected:

```text
HTTP/1.1 200 OK
Content-Type: application/json

[...]
```
