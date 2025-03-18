Problem 1-4 : NorthWinddatset https://relational.fit.cvut.cz/dataset/Northwind
How to download the dataset

To download the dataset you need to create connection in your mysql workbench

The datasets are publicly available directly from MariaDB database.

Open your favourite MariaDB client (MySQL Workbench) Use following credentials:
  hostname: relational.fit.cvut.cz
  port: 3306
  username: guest
  password: relational
Drive link: https://drive.google.com/drive/folders/1FMi6g1KDHbn17ikJSi7bE9-THywlxhdu?usp=sharing
Q-1: Rank Employee in terms of revenue generation. Show employee id, first name, revenue, and rank
Q-2: Show All products cumulative sum of units sold each month.
Q-3: Show Percentage of total revenue by each suppliers
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