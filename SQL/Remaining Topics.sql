SELECT * FROM db.undergrad;

-- Finding null values
SELECT * FROM db.undergrad
WHERE State IS NULL;

SELECT * FROM db.undergrad
WHERE State IS NOT NULL;
-- We have to specify "IS NOT NULL" and not "NOT NULL"


-- LIMIT Clause
SELECT * FROM db.undergrad
LIMIT 3;

SELECT * FROM Customers 
LIMIT 2,3; -- starting from 2nd index (0 based) and show next 3 records


-- Aggregate Function - Aggregate functions ignore null by default values (except for COUNT()).
SELECT MIN(State) -- MIN(*) is not valid
FROM db.undergrad; -- "MIN", "MAX", "COUNT" functions also used without groupby

SELECT COUNT(State) -- COUNT(*) is valid
FROM db.undergrad;

-- SUM() With an Expression
SELECT SUM(Value * Year)
FROM db.undergrad;

-- BETWEEN Text Values
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
-- selects all products with a ProductName `alphabetically` between Carnarvon Tigers and Mozzarella di Giovanni

-- BETWEEN Dates
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';


-- CASE Expression
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;