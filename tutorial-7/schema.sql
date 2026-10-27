-- ====================================================================
-- CS543 Web Services · Campus Library Schema & Seed Script
-- Database: gqldemo
-- Based on CS543 Tutorial 07 (Dr. Pramit Mazumdar, IIIT Vadodara)
-- ====================================================================

-- 1. Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS gqldemo;
USE gqldemo;

-- 2. Drop existing tables if re-running from scratch to avoid foreign key conflicts
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- 3. Create the 'authors' table
-- Each author has an auto-increment ID, required name, and optional country
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Create the 'books' table
-- Each book has an auto-increment ID, required title, publication year,
-- and a foreign key author_id linking to authors(id)
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    year INT,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. Seed initial tutorial data
-- Initial authors required by CS543 tutorial
INSERT INTO authors (name, country) VALUES
    ('Asha Patel', 'India'),
    ('Ravi Kumar', 'India');

-- Initial books required by CS543 tutorial
-- Author ID 1 = Asha Patel
-- Author ID 2 = Ravi Kumar
INSERT INTO books (title, year, author_id) VALUES
    ('Databases 101', 2020, 1),
    ('SQL in Practice', 2022, 1),
    ('Web Services Basics', 2023, 2);

-- 6. Verification queries (uncomment if running manually in MySQL CLI)
-- SELECT * FROM authors;
-- SELECT * FROM books;
