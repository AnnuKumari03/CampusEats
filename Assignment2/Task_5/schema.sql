-- CampusEats Database Schema


-- 1.User & Auth Service

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL,
    created_at TIMESTAMP
);

-- 2. ADMIN & VENDOR SERVICE

CREATE TABLE vendors (
    vendor_id INT PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(150),
    phone VARCHAR(20),
    status VARCHAR(30)
);

CREATE TABLE admins (
    admin_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    role VARCHAR(30) NOT NULL
);


---3. CATALOGUE SERVICE

CREATE TABLE MENU(
    menu_id INT PRIMARY KEY,
    vendor_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) NOT NULL,
    availability BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id)
);

-- 4. CART & ORDER SERVICE

CREATE TABLE cart(
    cart_id INT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) 
);

CREATE TABLE cart_items(
    cart_item_id INT PRIMARY KEY,
    cart_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY(cart_id) REFERENCES cart(cart_id),
    FOREIGN KEY (item_id) REFERENCES MENU(menu_id)
);

CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    total_amount DECIMAL(10,2)NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_At TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
    
);

CREATE TABLE order_items(
        order_item_id INT PRIMARY KEY,
        order_id INT NOT NULL,
        item_id INT NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        FOREIGN KEY(order_id) REFERENCES orders(order_id),
        FOREIGN KEY (item_id) REFERENCES MENU(menu_id)
);

--5.PAYMENT SERVICE

CREATE TABLE payments(
    payment_id INT PRIMARY KEY,
    order_id INT NOT NULL UNIQUE,
    amount DECIMAL(10,2)NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    status VARCHAR(30) NOT NULL,
    paid_at TIMESTAMP,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)

);

-- 6.REVIEW SERVICE

CREATE TABLE reviews(
    review_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_id INT NOT NULL,
    rating INT NOT NULL ,
    comment VARCHAR(500),
    created_At TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);


