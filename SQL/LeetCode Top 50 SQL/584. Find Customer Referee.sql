# Write your MySQL query statement below
SELECT name 
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;

# Rows where referee_id is NULL will not appear in the result. This is because in SQL, any comparison with NULL (such as referee_id <> 2) does not return TRUE or FALSE, but UNKNOWN. Only rows where the WHERE condition evaluates to TRUE are included in the result set, so rows with NULL in referee_id are excluded.