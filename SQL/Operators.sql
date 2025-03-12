CREATE DATABASE IF NOT EXISTS dml;
USE dml;

SELECT * FROM smartphones;

-- Arithmatic Operators
SELECT 
price + 10, price - 10, price * 10, price / 10, price % 10
FROM smartphones;

-- Bitwise Operators
SELECT 
price & 10, price | 10, ~ price, price << 2, price >> 2
FROM smartphones;

-- Comparison Operators
SELECT * FROM smartphones
WHERE (price >= 0 and price <= 10000000) or (has_nfc <> "False");

-- Logical Operators
-- 1. ALL - If a price value greater than all the values returned by subquery then it will get returned
SELECT * FROM smartphones
WHERE price > ALL(SELECT price FROM smartphones WHERE lower(processor_brand) = 'snapdragon');

-- 2. ANY - If a price value greater than any of the values returned by subquery then it will get returned
SELECT * FROM smartphones
WHERE price > ANY(SELECT price FROM smartphones WHERE lower(processor_brand) = 'snapdragon');
SELECT * FROM smartphones
WHERE price > SOME(SELECT price FROM smartphones WHERE lower(processor_brand) = 'snapdragon');

-- 3. BETWEEN 
SELECT * FROM smartphones
WHERE price BETWEEN 0 AND 10000;

-- 4. EXISTS - Presence of any record in the subquery
SELECT * FROM smartphones
WHERE EXISTS(SELECT price FROM smartphones WHERE lower(processor_brand) = 'snapdragon');

-- 5. IN/NOT IN
SELECT * FROM smartphones
WHERE price IN (10000, 20000, 30000, 50000);

-- 6. IS NULL
SELECT * FROM smartphones
WHERE price IS NULL; -- IS NOT NULL

-- String Concatination Operator - Not in MYSQL
SELECT brand_name || ' ' || model FROM smartphones; 