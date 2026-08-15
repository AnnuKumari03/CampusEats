Group- 10
Team Leader:Annu Kumari
Team Member 1 : Akanksha Upadhayay
Team Menber 2: Prerna

# CampusEats

CampusEats is a web services project being developed by a team of three MCA
students at IIIT Vadodara.

The goal of CampusEats is to provide a centralized web service for campus
food services. Students can discover food options, browse menus, place
orders, and track their orders through a web-based system.

## Project Objectives

- Build a practical RESTful web service.
- Learn and apply HTTP and REST principles.
- Provide versioned APIs under `/v1`.
- Use a SQL database for persistent data.
- Implement authentication and authorization.
- Validate JSON request data.
- Provide consistent error responses.
- Document APIs using OpenAPI and Swagger UI.
- Add automated API testing.
- Apply caching, pagination, rate limiting, and reliability techniques.
- Deploy the application so it can be accessed over the internet.

## Main Users

### Students

Students can:

- Register and log in.
- View restaurants and food stalls.
- Browse menus.
- Search for food items.
- Place orders.
- View order history.
- Track order status.

### Restaurant/Canteen Staff

Staff can:

- Manage menu items.
- Update prices and availability.
- View incoming orders.
- Update order status.

### Administrator

The administrator can:

- Manage users.
- Manage restaurants and canteens.
- Monitor orders.
- Manage the overall system.

## Planned API Resources

The REST API will use resource-oriented URLs such as:

```text
/v1/users
/v1/restaurants
/v1/menu-items
/v1/orders
/v1/order-items
```

Example operations:

```text
GET    /v1/restaurants
GET    /v1/restaurants/{id}
POST   /v1/restaurants
GET    /v1/menu-items
POST   /v1/orders
GET    /v1/orders/{id}
PATCH  /v1/orders/{id}
```

## Technology Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Node.js
- Express.js

### Database

- SQL database

### Web Service Technologies

- REST
- JSON
- XML content negotiation
- GraphQL
- SOAP/WSDL integration

### Development Tools

- Git and GitHub
- curl
- Postman
- Jest
- Supertest
- OpenAPI
- Swagger UI
- Docker

## Team Structure

The project has three members.

### Member 1 — Backend/API

- REST API implementation
- Express.js services
- Authentication and authorization
- Error handling
- HTTP status codes

### Member 2 — Database/Testing

- SQL database design
- Parameterized queries
- Database integration
- Automated tests
- Test data

### Member 3 — Frontend/Documentation

- HTML/CSS/JavaScript interface
- API integration
- OpenAPI documentation
- Swagger UI
- Project documentation

All members will contribute through Git commits.

## Development Roadmap

1. Project and Git setup
2. Database design and implementation
3. REST API implementation
4. Authentication and authorization
5. Validation and error handling
6. Caching and pagination
7. Rate limiting and reliability
8. OpenAPI and Swagger documentation
9. GraphQL endpoint
10. SOAP/WSDL integration
11. Automated testing
12. Docker containerization
13. Deployment

## Repository Structure

```text
campuseats/
│
├── README.md
│
└── docs/
    └── project-brief.md
```

More source-code folders will be added as development progresses.

## Project Status

🚧 **Under Development**

CampusEats is being developed incrementally as part of the Web Services
course. Features and documentation will be added through separate Git
commits as the project progresses.
