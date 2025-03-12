-- ORDER BY clause
SELECT * FROM flipcart.category
ORDER BY category ASC; -- Default Ascending

SELECT * FROM flipcart.category
ORDER BY category DESC;

-- GROUP BY clause
SELECT category, MAX(category_id) AS "max_id"
FROM flipcart.category
GROUP BY category
ORDER BY category;

-- WHERE clause
SELECT *
FROM flipcart.category
WHERE category = "Clothing";

-- HAVING Clause
SELECT category, MAX(category_id) AS "max_id"
FROM flipcart.category
WHERE category = "Clothing"
GROUP BY category
HAVING max_id > 50