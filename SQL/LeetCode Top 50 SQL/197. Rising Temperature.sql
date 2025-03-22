# Write your MySQL query statement below
SELECT T.id FROM (SELECT *,
LAG(temperature) OVER(ORDER BY recordDate) AS prev_temperature,
LAG(recordDate) OVER(ORDER BY recordDate) AS prev_date
FROM Weather) AS T
WHERE T.prev_temperature < T.temperature AND DATEDIFF(T.recordDate,T.prev_date) = 1;