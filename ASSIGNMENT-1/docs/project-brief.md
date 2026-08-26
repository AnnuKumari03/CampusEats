# CampusEats — Project Brief

## 1. Project Overview

CampusEats is a web service designed for students and campus users to discover
and manage food options available around a college campus.

The system will provide RESTful APIs that allow users to view restaurants,
browse menus, place food orders, and track their order status.

The project is being developed by a team of three MCA students as a Web
Services course project at IIIT Vadodara.

## 2. Problem Statement

Students often have to check different food stalls or canteens to find
available food, prices, and order status. CampusEats aims to provide one
centralized web service for these activities.

## 3. Main Users

### Students

Students can:

- Register and log in.
- View available restaurants or food stalls.
- Browse menus.
- Search for food items.
- Place orders.
- View their order history.
- Track order status.

### Restaurant/Canteen Staff

Staff can:

- Manage food items.
- Update prices and availability.
- View incoming orders.
- Update order status.

### Administrator

The administrator can:

- Manage users.
- Manage restaurants/canteens.
- Monitor orders.
- Manage the overall system.

## 4. Main Resources

The REST API will be organized around resources rather than action-based URLs.

Possible resources include:

- `/v1/users`
- `/v1/restaurants`
- `/v1/menu-items`
- `/v1/orders`
- `/v1/order-items`

Example:

```text
GET    /v1/restaurants
GET    /v1/restaurants/{id}
POST   /v1/restaurants
GET    /v1/menu-items
POST   /v1/orders
GET    /v1/orders/{id}
PATCH  /v1/orders/{id}
```

## 5. Proposed Technology Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Node.js
- Express.js

### Database

- SQL database

### API Format

- REST
- JSON
- Optional XML content negotiation

### Development and Testing

- Git and GitHub
- Postman/curl
- Jest and Supertest
- Swagger UI / OpenAPI
- Docker

## 6. Team Responsibilities

### Member 1 — Backend and API

Responsible for:

- REST API design
- Express.js services
- HTTP status codes
- Authentication
- Error handling

### Member 2 — Database and Testing

Responsible for:

- SQL database design
- Parameterized queries
- Database integration
- Automated API tests
- Test data

### Member 3 — Frontend and Documentation

Responsible for:

- HTML/CSS/JavaScript interface
- API integration
- OpenAPI documentation
- Swagger UI
- Project documentation

All three members will contribute through Git commits and code reviews.

## 7. Development Plan

### Phase 1 — Project Setup

- Create Git repository.
- Define project structure.
- Prepare README and documentation.
- Set up Node.js and Express.

### Phase 2 — Database

- Design database tables.
- Add users, restaurants, menu items, and orders.
- Use parameterized SQL queries.

### Phase 3 — REST API

- Implement versioned `/v1` endpoints.
- Add correct HTTP methods and status codes.
- Add JSON validation.
- Add consistent error responses.

### Phase 4 — Security

- Add JWT authentication.
- Implement authorization.
- Configure CORS deliberately.
- Add rate limiting.

### Phase 5 — Reliability

- Add request timeouts.
- Add retry with increasing backoff where appropriate.
- Add a circuit breaker for outbound services.
- Add structured logging and correlation IDs.

### Phase 6 — API Documentation and Testing

- Create a hand-written OpenAPI document.
- Serve Swagger UI from the application.
- Add automated tests using Jest and Supertest.
- Test success and error cases.

### Phase 7 — Advanced Web Service Features

- Add ETag and `304 Not Modified`.
- Configure Cache-Control for GET requests.
- Add cursor-based pagination.
- Add content negotiation for JSON/XML.
- Add GraphQL alongside the REST API.
- Demonstrate one SOAP/WSDL integration if required by the course.

### Phase 8 — Deployment

- Containerize the application using Docker.
- Use environment-based configuration.
- Deploy the service so that it is reachable over the internet.

## 8. Expected Outcome

The final CampusEats system will demonstrate practical knowledge of modern
web services, REST API design, databases, authentication, testing,
documentation, reliability, and deployment.

The project will also provide a strong portfolio example because it combines
frontend development, backend services, database programming, API design,
testing, and deployment.
