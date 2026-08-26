# CampusEats Brief

## What

CampusEats is a campus food ordering and management system that makes it easier for students to find and order food on campus. Students can browse food vendors, view menus and prices, select food items, place orders, make payments, and track their order status. Food vendors can manage their menus and process incoming orders. Campus administrators can manage users, vendors, and overall system activities.

The main goal of CampusEats is to provide a convenient digital platform that connects students with campus food services and reduces waiting time at food stalls.

## Who

The main users of CampusEats are:

- **Students:** Browse menus, search for food, add items to a cart, place orders, pay, and track orders.
- **Food Vendors:** Manage menus, update food availability, receive orders, accept or reject orders, and update order status.
- **Campus Administrators:** Manage users and vendors, monitor orders, and maintain the overall system.
### 1. Student / Customer

Students are the main users of CampusEats. They can:

- Create an account and log in.
- Browse restaurants and canteens.
- View menus and food details.
- Search for food items.
- Check availability and prices.
- Place orders.
- View their previous orders.
- Track the current status of an order.

### 2. Restaurant / Canteen Staff

Staff members manage the food service side of the application. They can:

- Create and update menu items.
- Change food prices.
- Mark items as available or unavailable.
- View incoming orders.
- Accept and update orders.
- Change order status.

### 3. Administrator

The administrator manages the overall platform. They can:

- Manage users.
- Manage restaurants and canteens.
- Monitor orders.
- Manage system data.
- Control access to administrative operations.

---

# Nouns — Things / Services / Resources

The following nouns represent the main resources in CampusEats:

1. **User** — a person registered in the system.
2. **Student** — a customer who uses the service to order food.
3. **Restaurant** — a campus food outlet or canteen.
4. **Menu** — the collection of food items offered by a restaurant.
5. **Menu Item** — an individual food product with details such as name,
   price, description, and availability.
6. **Order** — a food order created by a student.
7. **Order Item** — a particular menu item included in an order.
8. **Order Status** — the current state of an order, such as pending,
   accepted, preparing, ready, or completed.
9. **Authentication Token** — a token used to identify an authenticated user.
10. **API Request** — a request sent by a client to access or modify a
    CampusEats resource.
11. **API Response** — the result returned by the CampusEats service.
12. **Notification** — information sent to a user about relevant order or
    service updates.

Possible REST resource paths include:

```text
/v1/users
/v1/restaurants
/v1/menu-items
/v1/orders
/v1/order-items
```

---

# Verbs — Actions / Tasks / Contracts

The following verbs represent the main operations provided by CampusEats:

1. **Register** — create a new user account.
2. **Login** — authenticate a user.
3. **Logout** — end an authenticated session.
4. **View** — retrieve information about restaurants, menus, users, or orders.
5. **Search** — find restaurants or menu items.
6. **Create** — create a restaurant, menu item, or order.
7. **Update** — modify existing resource information.
8. **Delete** — remove a resource when the user has permission.
9. **Add** — add a menu item to an order.
10. **Place** — submit a food order.
11. **Accept** — accept an incoming order.
12. **Prepare** — move an accepted order into preparation.
13. **Mark Ready** — indicate that an order is ready for collection.
14. **Complete** — mark an order as completed.
15. **Cancel** — cancel an eligible order.
16. **Track** — retrieve the current status of an order.
17. **Validate** — check whether incoming request data is valid.
18. **Authenticate** — verify the identity of a user.
19. **Authorize** — check whether a user has permission to perform an action.
20. **Paginate** — retrieve large collections in smaller pages.
21. **Cache** — temporarily store suitable GET responses.
22. **Rate Limit** — control excessive API requests.
23. **Document** — describe API contracts using OpenAPI.
24. **Test** — verify API behavior automatically.

## Example API Contracts

```text
GET    /v1/restaurants
GET    /v1/restaurants/{id}
GET    /v1/restaurants/{id}/menu-items

POST   /v1/orders
GET    /v1/orders/{id}
PATCH  /v1/orders/{id}
DELETE /v1/orders/{id}
```

The API will use HTTP methods according to the operation being performed.
For example, `GET` retrieves resources, `POST` creates resources, `PATCH`
updates part of a resource, and `DELETE` removes a resource.



## Summary

CampusEats connects students, campus food outlets, and administrators through
a single web-service platform. Its **nouns** define the resources and data
managed by the system, while its **verbs** define the operations that users
and clients can perform on those resources. The project therefore provides a
clear foundation for designing REST APIs and demonstrating practical web
services concepts.