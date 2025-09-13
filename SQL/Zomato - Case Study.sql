-- Randomly select 5 rows from users table - df.sample(5) from pandas
SELECT * FROM zomato.users
ORDER BY rand()
LIMIT 5; 

-- Finding the rows which include atleast 1 null value
SELECT * FROM zomato.orders
WHERE restaurant_rating = ""; -- for null values command `restaurant_rating IS NULL`

-- Replacing null values with empty string
UPDATE zomato.orders
SET restaurant_rating = "Null" WHERE restaurant_rating = "";
SELECT * FROM zomato.orders;

-- Find number of orders placed by each customer
SELECT T1.user_id, T1.name, COUNT(*) FROM zomato.users AS T1
INNER JOIN zomato.orders AS T2 
WHERE T1.user_id = T2.user_id -- If you not mention the `where` clause the join becomes cross join
GROUP BY T1.user_id, T1.name;

-- Find the restaurant with most number of menu items
SELECT T2.r_id, T1.r_name, COUNT(*) AS freq FROM zomato.restaurants AS T1
INNER JOIN zomato.menu AS T2
ON T1.r_id = T2.r_id
GROUP BY T2.r_id, T1.r_name -- HAVING accessing the columns name mentioned in the select statment even though the QEO of having is before select?
ORDER BY freq DESC
LIMIT 1;

-- Find the number of votes and average rating for all the restaurants
SELECT T1.r_id, T2.r_name, COUNT(*) AS 'Votes', AVG(T1.restaurant_rating) AS 'avg_rating' 
FROM zomato.orders AS T1
INNER JOIN zomato.restaurants AS T2
ON T1.r_id = T2.r_id
WHERE T1.restaurant_rating <> "" -- IS NOT NULL
GROUP BY T1.r_id, T2.r_name;

-- Find the food that is being ordered by most number of customers
SELECT T3.f_id, T3.f_name, COUNT(*) AS freq
FROM zomato.orders AS T1
INNER JOIN zomato.menu AS T2
ON T1.r_id = T2.r_id
INNER JOIN zomato.food AS T3
ON T2.f_id = T3.f_id
GROUP BY T3.f_id, T3.f_name
ORDER BY freq DESC
LIMIT 1;

-- Find reataurant with max_revenue in a given month
WITH T AS (
	SELECT T1.r_id, T2.r_name, MONTH(T1.date) AS month, SUM(amount) AS total_amount
	FROM zomato.orders AS T1
	INNER JOIN zomato.restaurants AS T2
	ON T1.r_id = T2.r_id
	GROUP BY T1.r_id, T2.r_name, MONTH(T1.date)
)
SELECT *
FROM T
WHERE (month, total_amount) IN (
	SELECT month, MAX(total_amount)
	FROM T
	GROUP BY month
);

-- Find restaurants with total sales > avg(sales of all the restaurants)
SELECT T1.r_id, T2.r_name, SUM(T1.amount) AS total_revenue
FROM zomato.orders AS T1
INNER JOIN zomato.restaurants AS T2
ON T1.r_id = T2.r_id
GROUP BY T1.r_id, T2.r_name
HAVING SUM(T1.amount) > (SELECT AVG(amount) FROM zomato.orders);

