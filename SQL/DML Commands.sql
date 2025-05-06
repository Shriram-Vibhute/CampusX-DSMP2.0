-- Data Manipulation Languages (DML) Commands

CREATE TABLE IF NOT EXISTS dml_commands(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    branch VARCHAR(255) NOT NULL
);

-- INSERT
INSERT INTO dml_commands() -- There is no need to mention the () if you are inserting in all the columns 
VALUES (1, 'jonny', 'IT'), (2, 'DEX', 'CS'), (3, 'SAM', 'MEAH');

-- Different Ways of Insertion
-- 1. Inserting into All Columns
CREATE TABLE users (id INT, name VARCHAR(50), age INT);
INSERT INTO users
VALUES (1, 'John Doe', 30);

-- 2. Inserting into Specific Columns
CREATE TABLE users (id INT AUTO_INCREMENT, name VARCHAR(50), age INT);
INSERT INTO users (name, age)
VALUES ('Jane Doe', 28);

-- 3. Inserting Multiple Rows at Once
CREATE TABLE customers (name VARCHAR(50), age INT, country VARCHAR(50));
INSERT INTO customers (name, age, country)
VALUES
    ('Mike', 35, 'USA'),
    ('Emma', 22, 'UK'),
    ('Tom', 40, 'Canada');

-- 4. Inserting from Another Table - (IMP)
CREATE TABLE new_customers (name VARCHAR(50), age INT);
CREATE TABLE old_customers (name VARCHAR(50), age INT);

INSERT INTO new_customers (name, age) -- Dont need to write `VALUES` here
SELECT name, age
FROM old_customers;

-- 5. Inserting with Default Values
CREATE TABLE users (id INT AUTO_INCREMENT, name VARCHAR(50), age INT DEFAULT 18);
INSERT INTO users (name)
VALUES ('Alex');

-- DELETE
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dml_commands
WHERE name = 'DEX';

-- UPDATE
UPDATE dml_commands
SET name = 'new_name', branch = 'ABC' -- Multiple Updations
WHERE id = 1;

-- DELETE and UPDATE are perminant Querries

SELECT * FROM dml_commands; -- SELECT is a DQL command

-- Creating new column with default values
SELECT
brand_name, 'smartphone' AS 'phone' -- `phone` is col name and `smartphone` is default value
from dml.smartphones;