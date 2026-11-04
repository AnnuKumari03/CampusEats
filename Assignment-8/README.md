# CampusEats Catalogue — Assignment 8

## 1. Introduction

The CampusEats Catalogue is a menu management web application designed to simulate the backend and frontend workflows of a campus food service. The main focus of this project is to implement and demonstrate RESTful API principles using Node.js and Express.js.

This application allows users to view the entire menu, fetch a single item by ID, create a new menu item, and delete an item from the catalogue. The project also includes a simple front-end interface to interact with the API and display the menu data dynamically.

## 2. Team Details

Team Leader: Annu Kumari (20251651024)

Team Members:
- Prerna (20251651072)
- Akanksha Upadhyay (20251651011)

## 3. Objective

The objective of this assignment is to build a basic REST API for a catalogue service and understand how request parameters, request bodies, JSON parsing, and HTTP status codes work in Express.js. It also demonstrates how a frontend can communicate with a backend to perform CRUD-style operations.

## 4. Technologies Used

- Node.js
- Express.js
- HTML
- CSS
- JavaScript
- In-memory array-based database

## 5. Functionalities Implemented

- View all menu items using `GET /items`
- View a specific item using `GET /items/:id`
- Add a new dish to the catalogue using `POST /items`
- Delete an item using `DELETE /items/:id`
- Validate required input before creating a new item
- Display the updated menu on the front-end after actions are performed

## 6. API Endpoints and Behavior

| Method | Route | Description |
| --- | --- | --- |
| GET | `/items` | Returns all items in the catalogue |
| GET | `/items/:id` | Returns one item matching the provided ID |
| POST | `/items` | Creates a new item in the catalogue |
| DELETE | `/items/:id` | Deletes the selected item |

## 7. HTTP Status Codes Used

- `200 OK` — successful retrieval of data
- `201 Created` — successful creation of a new item
- `404 Not Found` — requested item ID does not exist
- `422 Unprocessable Entity` — required `name` field is missing or empty
- `204 No Content` — successful deletion of an item

## 8. Request Handling in Express

- `req.params` is used in `GET /items/:id` to access the dynamic route parameter value from the URL.
- `req.body` is used in `POST /items` to read the JSON payload sent by the client.
- `app.use(express.json())` is used so Express can parse request body data before it is accessed.

Example:

```javascript
app.get('/items/:id', (req, res) => {
  const item = items.find(i => i.id === Number(req.params.id));
});
```

```javascript
app.post('/items', (req, res) => {
  const { name, price, available } = req.body;
});
```

## 9. Project Structure

```text
catalogue/
├── public/
│   ├── index.html
│   └── style.css
├── server.js
├── package.json
├── README.md
├── main page.png
├── all items json.png
├── single item json.png
├── new item added using POST.png
├── Test 404 response.png
├── after adding.png
├── after delete.png
└── node_modules/
```

## 10. Setup and Run Instructions

1. Open the project folder.
2. Install dependencies:

```bash
npm install
```

3. Start the server:

```bash
node server.js
```

4. Open the browser and visit:

```text
http://localhost:3000
```

## 11. Screenshots / Demonstration

The screenshots below demonstrate the successful working of the application:

- Home page: [main page.png](./main%20page.png)
- All items JSON response: [all items json.png](./all%20items%20json.png)
- Single item JSON response: [single item json.png](./single%20item%20json.png)
- New item created using POST: [new item added using POST.png](./new%20item%20added%20using%20POST.png)
- 404 error response: [Test 404 response.png](./Test%20404%20response.png)
- After adding a new item: [after adding.png](./after%20adding.png)
- After deleting an item: [after delete.png](./after%20delete.png)

## 12. Conclusion

This project successfully demonstrates how to build and deploy a simple REST API in Node.js using Express.js. It covers key web development concepts such as route handling, JSON requests, validation, status codes, and communication between frontend and backend. The assignment provides a practical understanding of how a catalogue-based service can be implemented and tested in a real-world application environment.

## 13. Submission Note

This README file has been prepared for the final submission of the CampusEats Catalogue assignment and includes the project description, implementation details, API specification, setup instructions, and verification screenshots.
