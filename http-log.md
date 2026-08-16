# HTTP Request/Response Log
# Request 1 - Get User 1

### Request 

```bash 
curl -i https://jsonplaceholder.typicode.com/users/1

``` markdown 
## Response 

akankshanupadhyay@Aku-MacBook-Air campuseats % curl -i https://jsonplaceholder.typicode.com/users/1
HTTP/2 200 
date: Thu, 13 Aug 2026 17:59:59 GMT
content-type: application/json; charset=utf-8
content-length: 509
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"1fd-+2Y3G3w049iSZtw5t1mzSnunngE"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=KhMZYXBAOlfBzOwwYdQ%2Bg4NP1gs%2BsWmo22i0RfreV0k%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786642364"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=KhMZYXBAOlfBzOwwYdQ%2Bg4NP1gs%2BsWmo22i0RfreV0k%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786642364"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786642391
age: 1635
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2a99de399dd85fd-BOM
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
}%  

``` markdown
### Annotation

Status 200:The request was successful and the requested user data was returned.

Content-Type: application/json: The response body is in JSON format.


```
# Request 2 - Get User 2

### Request 

```bash 
curl -i https://jsonplaceholder.typicode.com/users/2

``` markdown 
## Response 

akankshanupadhyay@Aku-MacBook-Air campuseats % curl -i https://jsonplaceholder.typicode.com/users/2
HTTP/2 200 
date: Thu, 13 Aug 2026 18:09:19 GMT
content-type: application/json; charset=utf-8
content-length: 509
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"1fd-XTG63SYhaP/Uo6/vgmARnL3rpBk"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=QPAnKfzcZr%2B7jt4zABk8fHJbUmVPE%2Bq0YRdhLldcR%2Fw%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786328764"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=QPAnKfzcZr%2B7jt4zABk8fHJbUmVPE%2Bq0YRdhLldcR%2Fw%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786328764"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 948
x-ratelimit-reset: 1786328814
age: 13801
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2a9ab8fdacbd91f-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}% 

``` mark
### Annotation

Status 200: The request was successful and the requested user data was returned.
Content-Type: application/json:The response body is in JSON format.


###
```mark
# Request 3 - Get User 3
###Request

akankshanupadhyay@Aku-MacBook-Air campuseats % curl -i https://jsonplaceholder.typicode.com/users/3
HTTP/2 200 
date: Thu, 13 Aug 2026 18:14:09 GMT
content-type: application/json; charset=utf-8
content-length: 520
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"208-uuwhfwQMzFzbJr9Pg6DKXae0SXA"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=pTHYtZhRs%2B%2FGKt0uEp0uofGuJZYjDE%2BCAP0Nev8Mchk%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786261563"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=pTHYtZhRs%2B%2FGKt0uEp0uofGuJZYjDE%2BCAP0Nev8Mchk%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786261563"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786261615
accept-ranges: bytes
cf-cache-status: REVALIDATED
cf-ray: a2a9b2a2af5dd8f9-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 3,
  "name": "Clementine Bauch",
  "username": "Samantha",
  "email": "Nathan@yesenia.net",
  "address": {
    "street": "Douglas Extension",
    "suite": "Suite 847",
    "city": "McKenziehaven",
    "zipcode": "59590-4157",
    "geo": {
      "lat": "-68.6102",
      "lng": "-47.0653"
    }
  },
  "phone": "1-463-123-4447",
  "website": "ramiro.info",
  "company": {
    "name": "Romaguera-Jacobson",
    "catchPhrase": "Face to face bifurcated interface",
    "bs": "e-enable strategic applications"
  }
}% 

### Annotation

Status 200: The request was successful and the requested user data was returned.

Content-Type: application/json: The response body is in JSON format.

```mark

# Request 4 - Get User 4
###Request

akankshanupadhyay@Aku-MacBook-Air campuseats % curl -i https://jsonplaceholder.typicode.com/users/4
HTTP/2 200 
date: Thu, 13 Aug 2026 18:14:43 GMT
content-type: application/json; charset=utf-8
content-length: 525
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"20d-8RgvpSlsXJuYWj1NkFA2Hm1U5TI"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=Jms7u18JBZX9O7e79LT%2BDfBxd6BDKjHNlSCDKct6RNY%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786344646"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=Jms7u18JBZX9O7e79LT%2BDfBxd6BDKjHNlSCDKct6RNY%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786344646"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 997
x-ratelimit-reset: 1786344654
age: 5901
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2a9b37bae320b2c-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 4,
  "name": "Patricia Lebsack",
  "username": "Karianne",
  "email": "Julianne.OConner@kory.org",
  "address": {
    "street": "Hoeger Mall",
    "suite": "Apt. 692",
    "city": "South Elvis",
    "zipcode": "53919-4257",
    "geo": {
      "lat": "29.4572",
      "lng": "-164.2990"
    }
  },
  "phone": "493-170-9623 x156",
  "website": "kale.biz",
  "company": {
    "name": "Robel-Corkery",
    "catchPhrase": "Multi-tiered zero tolerance productivity",
    "bs": "transition cutting-edge web services"
  }
}%   

### Annotation

Status 200: The request was successful and the requested user data was returned.

Content-Type: application/json: The response body is in JSON format.

``` mark

  ## Request 5 → /users/999 → 404

akankshanupadhyay@Aku-MacBook-Air campuseats % curl -i https://jsonplaceholder.typicode.com/users/999
HTTP/2 404 
date: Thu, 13 Aug 2026 18:16:29 GMT
content-type: application/json; charset=utf-8
content-length: 2
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=oipP5vBMKKujV2a%2BfOkangJ0zFuhqZaUMUSn8l9mvj8%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786644989"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=oipP5vBMKKujV2a%2BfOkangJ0zFuhqZaUMUSn8l9mvj8%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786644989"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786645031
cf-cache-status: MISS
cf-ray: a2a9b60f5d6ccde3-BOM
alt-svc: h3=":443"; ma=86400

{}%  

### Annotation

- Status 404:The requested resource was not found.
- Content-Type: application/json: The response body is in JSON format.