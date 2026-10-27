# Campus Library

**CS543 Web Services — Tutorial 7**  
**Project:** Campus Library Management System  
**Technologies:** Node.js, Apollo Server, GraphQL, MySQL, HTML, and CSS

## Team

| Role | Name | Enrollment number |
|---|---|---|
| Team Leader | Annu Kumari | 20251651024 |
| Team Member | Prerna | 20251651072 |
| Team Member | Akanksha Upadhaya | 20251651011 |

## Project overview

Campus Library is a small web application for browsing authors and their books. It uses a GraphQL API built with Apollo Server to retrieve library data from MySQL and to add books. The browser interface displays authors and books and provides a form for adding a book to an author.

## Features

- View authors and their books, including publication years.
- Query authors, an individual author, and books through GraphQL.
- Add a book through a GraphQL mutation and save it in MySQL.
- Enforce the author-book relationship with a MySQL foreign key.
- Start with sample authors and books from the database setup script.

## Project structure

```text
CS543_TUT7_CampusLibrary/
├── db.js
├── package.json
├── schema.sql
├── server.js
├── .env.example
├── README.md
├── public/
│   ├── index.html
│   └── style.css
├── ss1.png
├── ss2.png
└── ss3.png
```

## Requirements

- Node.js 18 or newer
- MySQL Server 8.x or a compatible MySQL server
- A modern web browser
- VS Code Live Server extension (to serve the frontend)

## Setup and run

### 1. Create the database and sample data

From the project directory, open the MySQL command-line client:

```bash
mysql -u root -p
```

At the MySQL prompt, run the schema script using its full path. Replace the example path with the location of this project:

```sql
SOURCE C:/path/to/CS543_TUT7_CampusLibrary/schema.sql;
```

The script creates the `gqldemo` database, the `authors` and `books` tables, and sample rows. Its sample inserts can be run again without duplicating those rows.

### 2. Configure the database connection

Copy `.env.example` to `.env` in the project directory, then update the database credentials if needed:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=gqldemo
PORT=4000
```

For example, in PowerShell:

```powershell
Copy-Item .env.example .env
```

Set `DB_PASSWORD` to your local MySQL password. Do not include your real `.env` file when sharing or submitting the project.

### 3. Install dependencies and start the API

In the project directory, run:

```bash
npm install
npm start
```

The server should report that the GraphQL API is ready at `http://localhost:4000/`. Keep this terminal open while using the application. The URL also provides Apollo Sandbox for trying queries and mutations.

### 4. Open the frontend

In VS Code, open `public/index.html` with the Live Server extension. The page is typically served at `http://127.0.0.1:5500`. The API must be running at `http://localhost:4000/`.

## GraphQL examples

Retrieve authors and their books:

```graphql
query {
  authors {
    name
    country
    books {
      title
      year
    }
  }
}
```

Add a book:

```graphql
mutation {
  addBook(title: "GraphQL for Beginners", year: 2025, authorId: "2") {
    id
    title
    year
    author {
      name
    }
  }
}
```

## Screenshots

### MySQL sample data

![MySQL sample book data](ss1.png)

### GraphQL author query

![Apollo Sandbox author query](ss2.png)

### GraphQL add-book mutation

![Apollo Sandbox add-book mutation](ss3.png)

## Implementation summary

- **Database:** `authors` and `books` tables, connected by a one-to-many relationship and foreign key.
- **GraphQL queries:** `authors`, `author`, and `books`.
- **Relationship resolvers:** `Author.books` and `Book.author`.
- **GraphQL mutation:** `addBook`.
- **Frontend:** HTML and CSS interface that loads library data and submits the add-book mutation.

## Troubleshooting

- **Access denied for user:** Check `DB_USER` and `DB_PASSWORD` in `.env`.
- **Unknown database `gqldemo`:** Run `schema.sql` in MySQL.
- **Connection refused:** Make sure the MySQL service is running.
- **Port 4000 is already in use:** Set a different `PORT` in `.env` and update the `API` constant in `public/index.html` to use the same port.
- **Frontend cannot connect:** Confirm that the API is running and that the URL in `public/index.html` matches the API address.
