# HTTP Log — CampusEats Assignment

This log documents five read-only HTTP GET requests made with `curl.exe -i`
to the public JSONPlaceholder API.

> **Note:** `curl -i` displays the response headers followed by the response body.
> The five terminal captures below are reproduced from the supplied screenshots.

---

## 1. GET `/posts/1`

### Request

```bash
curl.exe -i https://jsonplaceholder.typicode.com/posts/1
```

### Full response

```text
Ps C:\Users\Dell\OneDrive\Desktop> curl.exe -i https://jsonplaceholder.typicode.com/posts/1

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 11:10:37 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 292

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"124-yikdLzq05gfBrJFrcdJ8YqOLGnU"

expires: -1

nel: {"report_to":"heroku-neL", "response_headers":["Via"] , "max_age": 3600, "success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache

report-to: {"group":"heroku-nel", "endpoints": [{"url":"https://nel.heroku. com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i21bjuoY%3D\u0026sid=e11707d5-02a7
—43ef—bU5e-2cf4d2036F7d\u0026ts=1785194657"}] , "max_age": 3600}

reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i21bjuoY%3D&s id=e11707d5-02a7-43ef—bu5e-2cf4d2036F7d&ts
=1785194657"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-Limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1785194663

Age: 2132

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2af839dcdbfaed9-BOM

alt-svc: h3=":443"; ma=86400

{
"userId": 1,
"id": 1,
"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",

"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem ev
eniet architecto"

}
PS C:\Users\Del1\OneDrive\Desktop>
```

### Annotation

- **Status:** `200 OK` — The request was successful and the requested post was returned.
- **Content-Type:** `application/json; charset=utf-8` — The response body is JSON data encoded using UTF-8.

---

## 2. GET `/posts/2`

### Request

```bash
curl.exe -i https://jsonplaceholder.typicode.com/posts/2
```

### Full response

```text
of

Ps C:\Users\Dell\OneDrive\Desktop> curl.exe -i https://jsonplaceholder.typicode.com/posts/2

HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 11:14:06 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 278

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"116-jnDuMpj ju89+9j7eOBqkdFsVRjs"

expires: -1

nel: {"report_to":"heroku-neL", "response_headers":["Via"] , "max_age": 3600, "success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache

report-to: {"group":"heroku-nel", "endpoints": [{"url":"https://nel.heroku. com/reports?s=AyDEJzv2CFP160WD%2F3Jd LYGmQ%2BrTTe1sKm7ePc248K0%3D\u0026sid=e11707d5—
02a7-43ef—bU5e-2cF4d2036F7d\u0026ts=1786352212"}] , "max_age" : 3600}

reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=AyDEJzv2CFP160WD%2F 3 Jd LYGmQ%2BrT Te1lskm7ePc248K0%3D&s id=e11707d5-02a7—43ef—bU5e-2cF4d2036F7
d&ts=1786352212"

Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-Limit: 1000

x-ratelimit-remaining: 952

x-ratelimit-reset: 1786352214

Age: 20772

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2af88b679bc84d7-BOM

alt-svc: h3=":443"; ma=86400

{

"userId": 1
"id": 2
"title "qui est esse",

"body est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut r

eiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"

}
PS C:\Users\Del1\OneDrive\Desktop>
```

### Annotation

- **Status:** `200 OK` — The request was successful and the requested post was returned.
- **Content-Type:** `application/json; charset=utf-8` — The response body is JSON data encoded using UTF-8.

---

## 3. GET `/users/1`

### Request

```bash
curl.exe -i https://jsonplaceholder.typicode.com/users/1
```

### Full response

```text
2
Ps C:\Users\Dell\OneDrive\Desktop> curl.exe -i https: //jsonplaceholder.typicode.com/users/1
HTTP/1.1 200 OK

Date: Fri, 14 Aug 2026 11:15:37 GMT

Content-Type: application/json; charset=ut#-8

Content-Length: 509

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"1fd-+2Y3G3u0u9iSZtw5timzSnunngE"

expires: -1

nel: {"report_t
pragma: no-cache
report-to: {"group
_age":3600}
Teporting-endpoints: heroku-nel="https: //nel. heroku. com/reports?s=T1P99NGKSRzfe0ODpCODLM8JWCEiHfhhhBQd%2FNRD3 jk%3D&s:id=e11707d5-62a7-U3ef-buSe-2cFud2036F7d&ts=1786354967"
Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-Limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1786354974

Age: 4710

Accept-Ranges: bytes

cf-cache-status: HIT

CF-RAY: a2af8aedfe12U13d-B0M

4u3"; ma=86400

9.1}

c"

600, "success_fraction":0.01, "failure_fractio!

eroku-ne ‘esponse_headers" "max_age

heroku-nel", "endpoints": [{"url": "https: //nel. heroku. com/reports?s=TLP99N6KsRzfeo0DpCODLM8 JWCEiHFhhhBQd%2FNRD3 jk%*3D\u0026sid=e11707d5-92a7-U3ef—bu5e-2cFud2936F7d\u9e26ts=1786354967"}] , "max

Leanne Graham",
"Bret",
Sincere@april.bi:

1-778-736-8031 x56442",
hildegard.org",
t

“Romaguera-Crona",
catchPhrase": "Multi-layered client-server neural-net"
bs": “harness real-time e-markets'
```

### Annotation

- **Status:** `200 OK` — The request was successful and the requested user was returned.
- **Content-Type:** `application/json; charset=utf-8` — The response body is JSON data encoded using UTF-8.

---

## 4. GET `/comments/1`

### Request

```bash
curl.exe -i https://jsonplaceholder.typicode.com/comments/1
```

### Full response

```text
s
} curl.exe -i https: //jsonplaceholder.typicode.com/comments/1
HTTP/1.1 260 OK1\OneDrive\Desktop>
Date: Fri, 14 Aug 2026 11:17:48 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 268
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"10c-KI4I9RM/+33TKdV8CFsIvqsDSP\
expires: -1
nel: {"report_to":"heroku-nel", "response_headers":["Via"] , "max_age":3600, "success_fraction":0.01, “failure_fraction":0.1}
pragma: no-cache
report-to: {"group"
ge": 3600}
reporting-endpoints: heroku-nel-:
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-Limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786693990
Age: 12292
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2af8e226ce9cb6e-BOM
alt-sv ma=86400

https: //nel. heroku.com/reports?s=j6eu6zLWJUKTPG1vq6F 7NyLUJ1ezgY9n jKNNbhU9XPg%3D\ue626sid=e11707d5-02a7-U3ef-buSe-2cFUd2036F7d\ue026ts=1786693975"}] , "max_a

186693975"

tps: //neL. heroku. com/reports?s=j6eu6zLWJUKTPG1Vq6F 7NyL4J1ezgY9njKNNbhU9XPg%3DSsid=e11707d5-62a7-U3ef—buse-2cFUd2036F7d8t:

1

d labore ex et quam laborum",
Eliseo@gardner. bi
audantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

3
Ps C:\Users\Dell\OneDrive\Desktop>
```

### Annotation

- **Status:** `200 OK` — The request was successful and the requested comment was returned.
- **Content-Type:** `application/json; charset=utf-8` — The response body is JSON data encoded using UTF-8.

---

## 5. Deliberate failure — GET `/posts/999999`

### Request

```bash
curl.exe -i https://jsonplaceholder.typicode.com/posts/999999
```

### Full response

```text
t

Ps C:\Users\Dell\OneDrive\Desktop> curl.exe -i https: //jsonplaceholder.typicode.com/posts/999999
HTTP/1.1 404 Not Found

Date: Fri, 14 Aug 2026 11:18:49 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 2

Connection: keep-alive

access-control-allow-credentials: true

Cache-Control: max-age=43200

etag: W/"2-vyGpé6PvFoURvsFtPoIWeCReyIC8"

expires: -1

nel: {"report_to'
pragma: no-cache
report-to: {"group
ax_age" :3600}
reporting-endpoints: heroku-nel="https: //nel. heroku.com/reports?s=pPi%2FMiavnH6z16Lk5KF9MWgWL YDnH%2FXRkxT mcr jBbO%3DSsid=e11707d5-G2a7-U3ef—bUSe-2cFud2036F7d&ts=1786706329"
Server: cloudflare

vary: Origin, Accept-Encoding

via: 2.0 heroku-router

x-content-type-options: nosniff

x-powered-by: Express

x-ratelimit-Limit: 1000

x-ratelimit-remaining: 999

x-ratelimit-reset: 1786706350

cf-cache-status: EXPIRED

CF-RAY: a2af8f9bcbc2738-BOM

alt-sv ma=86400

heroku-nel'

, "response_headers ax_age":3600, "success_fraction":0.01, "failure_fraction":0.1}

11707d5-62a7-43e f—buSe-2c FUd2636F7d\ue026ts=1786706329"}] , "Mm

"heroku-nel ‘/nel. heroku.com/reports?s=pPi%2FMiavnH6z16Lk5KF9MWgWLYDnH%2FXRkxTOMcr jBbO%3D\uee26si

"endpoint:
```

### Annotation

- **Status:** `404 Not Found` — The server could not find the requested resource. This was deliberately requested to satisfy the assignment's 404 requirement.
- **Content-Type:** `application/json; charset=utf-8` — The response body is JSON data encoded using UTF-8.

---

## Summary

| # | Request | Status | Content-Type |
|---|---|---|---|
| 1 | `GET /posts/1` | `200 OK` | `application/json; charset=utf-8` |
| 2 | `GET /posts/2` | `200 OK` | `application/json; charset=utf-8` |
| 3 | `GET /users/1` | `200 OK` | `application/json; charset=utf-8` |
| 4 | `GET /comments/1` | `200 OK` | `application/json; charset=utf-8` |
| 5 | `GET /posts/999999` | `404 Not Found` | `application/json; charset=utf-8` |

**API used:** JSONPlaceholder — a public, read-only JSON API used for testing and learning HTTP/API requests.
