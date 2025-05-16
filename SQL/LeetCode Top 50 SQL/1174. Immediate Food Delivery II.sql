# Write your MySQL query statement below
WITH T AS (
    SELECT (
        SELECT 
            CASE
                WHEN t2.order_date = t2.customer_pref_delivery_date THEN 'immediate'
                ELSE 'scheduled'
            END
        FROM Delivery AS t2
        WHERE t1.customer_id = t2.customer_id
        ORDER BY t2.order_date ASC
        LIMIT 1
    ) AS type
    FROM Delivery AS t1
    GROUP BY t1.customer_id
)
SELECT
    ROUND((SELECT COUNT(*) FROM T WHERE T.type = 'immediate') / COUNT(*) * 100, 2) AS immediate_percentage
FROM T