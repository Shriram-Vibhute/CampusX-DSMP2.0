-- 1: Rank Employee in terms of revenue generation. Show employee id, first name, revenue, and rank
SELECT nw_employees.EmployeeID, nw_employees.FirstName , sum(nw_order_details.UnitPrice * nw_order_details.Quantity) AS revenue,
RANK() OVER(ORDER BY sum(nw_order_details.UnitPrice * nw_order_details.Quantity) DESC) AS EmpRank
FROM nw_orders
INNER JOIN nw_order_details 
ON nw_order_details.OrderID = nw_orders.OrderID
INNER JOIN nw_employees 
ON nw_employees.EmployeeID = nw_orders.EmployeeID
GROUP BY nw_employees.EmployeeID, nw_employees.FirstName
ORDER BY EmpRank;

-- 2: Show All products cumulative sum of units sold each month. - IMP QUESTION
SELECT nw_products.ProductID, MONTH(nw_orders.OrderDate), SUM(nw_order_details.Quantity),
SUM(SUM(nw_order_details.Quantity)) OVER(PARTITION BY nw_products.ProductID ORDER BY MONTH(nw_orders.OrderDate) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM nw_products
INNER JOIN nw_order_details
ON nw_products.ProductID = nw_order_details.ProductID
INNER JOIN nw_orders
ON nw_order_details.OrderID = nw_orders.OrderID
GROUP BY nw_products.ProductID, MONTH(nw_orders.OrderDate);

-- 3: Show Percentage of total revenue by each suppliers
SELECT DISTINCT(T1.SupplierID),
SUM(T3.UnitPrice * T3.Quantity) OVER(PARTITION BY T1.SupplierID) * 100 / SUM(T3.UnitPrice * T3.Quantity) OVER()
FROM nw_suppliers AS T1
INNER JOIN nw_products AS T2
ON T1.SupplierID = T2.SupplierID
INNER JOIN nw_order_details AS T3
ON T2.ProductID = T3.ProductID;











Q-4: Show Percentage of total orders by each suppliers
Q-5:Show All Products Year Wise report of totalQuantity sold, percentage change from last year.
Problem 6 - 15
For the next problems, you can get the dataset as well as the details here (Use the cleaned csv file).

Problem-6: For each condition, what is the average satisfaction level of drugs that are "On Label" vs "Off Label"?
Problem-7: For each drug type (RX, OTC, RX/OTC), what is the average ease of use and satisfaction level of drugs with a price above the median for their type?
Problem 8: What is the cumulative distribution of EaseOfUse ratings for each drug type (RX, OTC, RX/OTC)? Show the results in descending order by drug type and cumulative distribution. (Use the built-in method and the manual method by calculating on your own. For the manual method, use the "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW" and see if you get the same results as the built-in method.)
Problem 9: What is the median satisfaction level for each medical condition? Show the results in descending order by median satisfaction level. (Don't repeat the same rows of your result.)
Problem 10: What is the running average of the price of drugs for each medical condition? Show the results in ascending order by medical condition and drug name.
Problem 11: What is the percentage change in the number of reviews for each drug between the previous row and the current row? Show the results in descending order by percentage change.
Problem 12: What is the percentage of total satisfaction level for each drug type (RX, OTC, RX/OTC)? Show the results in descending order by drug type and percentage of total satisfaction.
Problem 13: What is the cumulative sum of effective ratings for each medical condition and drug form combination? Show the results in ascending order by medical condition, drug form and the name of the drug.
Problem-14: What is the rank of the average ease of use for each drug type (RX, OTC, RX/OTC)? Show the results in descending order by rank and drug type.
Problem-15: For each condition, what is the average effectiveness of the top 3 most reviewed drugs?