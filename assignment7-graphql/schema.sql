
CREATE DATABASE IF NOT EXISTS campuseats_graphql;
USE campuseats_graphql;

CREATE TABLE IF NOT EXISTS menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO menu_items (name, category, price) VALUES
('Veg Burger', 'Fast Food', 80.00),
('Masala Dosa', 'South Indian', 100.00),
('Paneer Sandwich', 'Snacks', 90.00),
('Veg Pizza', 'Fast Food', 150.00);
