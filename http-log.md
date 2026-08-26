# HTTP Request/Response Log

## API Used

**JSONPlaceholder**

Base URL: `https://jsonplaceholder.typicode.com`

JSONPlaceholder is a public, read-only JSON API used for testing and learning HTTP requests.

> **Note:** The commands below were executed using `curl -i`. The `-i` option includes the HTTP response headers and response body in the terminal output. The command itself records the outgoing HTTP method and URL.

---

# Request 1 — GET `/posts/1`

## Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

**HTTP method:** `GET`  
**URL:** `https://jsonplaceholder.typicode.com/posts/1`

## Response

```text
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2026 14:33:20 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 292
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"124-yjKdLzQ5bfJrFcrdJ8Yq0LGnU"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=vm67FVLNHsCgrFfgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1785194657"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vm67FVLNHsCgrFfgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1785194657"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1785194663
Age: 26094
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2b0ac8d7c6ac116-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

## Annotation

- **Status: `200 OK`** — The server successfully processed the request and returned the requested resource.
- **Content-Type: `application/json; charset=utf-8`** — The response body is JSON data encoded using UTF-8.

---

# Request 2 — GET `/posts/2`

## Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/2
```

**HTTP method:** `GET`  
**URL:** `https://jsonplaceholder.typicode.com/posts/2`

## Response

```text
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2026 14:35:40 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 278
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"116-jmDu6ju89+9j7e0BqkdFsVRjs"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=iXrXLiMshk%2BpDyAfnrNUJFRE GdGA4ZlzQlCMxdFLz8w%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786349193"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=iXrXLiMshk%2BpDyAfnrNUJFREGdGA4ZlzQlCMxdFLz8w%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786349193"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786349214
Age: 28031
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2b0affbac07ff60-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}
```

## Annotation

- **Status: `200 OK`** — The server successfully processed the request and returned post 2.
- **Content-Type: `application/json; charset=utf-8`** — The response body contains JSON data encoded using UTF-8.

---

# Request 3 — GET `/posts/5`

## Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/5
```

**HTTP method:** `GET`  
**URL:** `https://jsonplaceholder.typicode.com/posts/5`

## Response

```text
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2026 14:37:03 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 225
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"e1-1ivojO0CtPZmcMK0iydTbsfG7Wc"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=v4TVdB2eugpI45xvP0IrLzA1cbh6VXU7iRPa3xXKW4%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786718223"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=v4TVdB2eugpI45xvP0IrLzA1cbh6VXU7iRPa3xXKW4%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786718223"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786718230
Age: 0
Accept-Ranges: bytes
cf-cache-status: MISS
CF-RAY: a2b0b1fb6c94ff68-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 5,
  "title": "nesciunt quas odio",
  "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nnest aut tenetur dolor neque"
}
```

## Annotation

- **Status: `200 OK`** — The requested post was successfully found and returned.
- **Content-Type: `application/json; charset=utf-8`** — The response contains JSON data encoded using UTF-8.

---

# Request 4 — GET `/users/1`

## Request

```bash
curl -i https://jsonplaceholder.typicode.com/users/1
```

**HTTP method:** `GET`  
**URL:** `https://jsonplaceholder.typicode.com/users/1`

## Response

```text
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2026 14:38:09 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"1fd-+2Y3G3w049iSZtw51mzSnunngE"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=c4W1UxriyoWTYFuUhbALz0rDzICU7r%2BRoXsXRciuS0Y%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786374767"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=c4W1UxriyoWTYFuUhbALz0rDzICU7r%2BRoXsXRciuS0Y%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786374767"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786374775
Age: 25076
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2b0b39b49d4c5da-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
```

## Annotation

- **Status: `200 OK`** — The server successfully found and returned the requested user resource.
- **Content-Type: `application/json; charset=utf-8`** — The response body is JSON data encoded using UTF-8.

---

# Request 5 — Deliberate 404

## Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/99999
```

**HTTP method:** `GET`  
**URL:** `https://jsonplaceholder.typicode.com/posts/99999`

## Response

```text
HTTP/1.1 404 Not Found
Date: Fri, 14 Aug 2026 14:39:49 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"2-vyGp6PvFo4RvsFtPoIweCReyIC8"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=968EtgLWKppnBiVORbr5i0tECH7GggNoaOLr%2FYyqDj8%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786690346"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=968EtgLWKppnBiVORbr5i0tECH7GggNoaOLr%2FYyqDj8%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786690346"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 995
x-ratelimit-reset: 1786690390
Age: 28042
cf-cache-status: HIT
CF-RAY: a2b0b60cdb100c0c-BOM
alt-svc: h3=":443"; ma=86400

{}
```

## Annotation

- **Status: `404 Not Found`** — The requested resource does not exist on the server.
- **Content-Type: `application/json; charset=utf-8`** — The response is represented as JSON data encoded using UTF-8.

---

# Summary

| # | HTTP Method | Endpoint | Status | Content-Type |
|---|---|---|---|---|
| 1 | GET | `/posts/1` | 200 OK | application/json; charset=utf-8 |
| 2 | GET | `/posts/2` | 200 OK | application/json; charset=utf-8 |
| 3 | GET | `/posts/5` | 200 OK | application/json; charset=utf-8 |
| 4 | GET | `/users/1` | 200 OK | application/json; charset=utf-8 |
| 5 | GET | `/posts/99999` | 404 Not Found | application/json; charset=utf-8 |

## Conclusion

Five read-only GET requests were made to the public JSONPlaceholder API.
Four requests successfully returned existing resources with `200 OK`.
The fifth request deliberately requested a non-existent resource and
returned `404 Not Found`.

All five responses used `application/json; charset=utf-8`, indicating
that the response body was formatted as JSON using UTF-8 encoding.
