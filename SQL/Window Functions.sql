create database db;
USE db;

CREATE TABLE marks(
	name VARCHAR(255),
    branch VARCHAR(255),
    marks INT
);

INSERT INTO marks (name,branch,marks)VALUES 
('Nitish','EEE',82),
('Rishabh','EEE',91),
('Anukant','EEE',69),
('Rupesh','EEE',55),
('Shubham','CSE',78),
('Ved','CSE',43),
('Deepak','CSE',98),
('Arpan','CSE',95),
('Vinay','ECE',95),
('Ankit','ECE',88),
('Anand','ECE',81),
('Rohit','ECE',95),
('Prashant','MECH',75),
('Amit','MECH',69),
('Sunny','MECH',39),
('Gautam','MECH',51);

SELECT * FROM marks;

-- Find the avg marks of all the student for their respective branch
select *, avg(marks) over(partition by branch) as avg_marks
from marks;

-- Find the minimum and max marks corrosopnding all the student as per there specific branch
select *, avg(marks) over(partition by branch), min(marks) over(partition by branch), max(marks) over(partition by branch)
from marks;

-- Find all the students who have marks higher then the avg of there respective branch
select t1.name, t1.marks, t1.avg_marks
from (select name, marks, avg(marks) over(partition by branch) as avg_marks from db.marks) as t1
where t1.marks > t1.avg_marks;

-- rank | dense_rank | row_number
select *,
rank() over(partition by branch order by marks desc) as 'rank', -- consider window branch_wise
dense_rank() over(order by marks desc) as 'row_rank' -- Consider a whole dataset as 1 window
from db.marks;

select *,
row_number() over(partition by branch order by marks desc) as 'row_rank' -- consider window branch_wise
from db.marks;

-- You have to find top 2 users from each month who have the total max bill in that month
with ref as(select monthname(date) as 'month_name', user_id, sum(amount) as total_amount,
			rank() over(partition by monthname(date) order by sum(amount) desc) as ranked_user
			from zomato.orders
			group by month_name, user_id
)
select * from ref
where ranked_user < 3;

-- first_value | last_value | nth_value 
-- Find the student who got highest marks in there respective branch
select *,
first_value(name) over(partition by branch order by marks desc)
from db.marks;


-- The concept of frames

select *,
last_value(name) over(partition by branch order by marks desc rows between unbounded preceding and current row)
from db.marks;
-- This is the default behavour - if you cannot mention `rows between unbounded preceding and current row`
-- meaning - From start to current row

select *,
last_value(name) over(partition by branch order by marks desc rows between unbounded preceding and unbounded following)
from db.marks;
-- `rows between unbounded preceding and unbounded following` - Complete Frame

select *,
last_value(name) over(partition by branch order by marks desc rows between 1 preceding and 1 following)
from db.marks;
-- `rows between unbounded preceding and unbounded following` - 1 row above and 1 row below

select *,
last_value(name) over(partition by branch order by marks desc rows between 1 preceding and 1 following)
from db.marks;

-- Find the branch topper
select name, branch, marks from db.marks
where (branch, marks) in (select branch, max(marks)
from db.marks
group by branch)
order by marks desc;

-- Using Window function
select name, branch, marks
from (select *,
first_value(name) over(partition by branch order by marks desc rows between unbounded preceding and unbounded following) as 'topper_name',
first_value(marks) over(partition by branch order by marks desc rows between unbounded preceding and 1 following) as 'topper_marks'
from db.marks) as t
where marks = t.topper_marks and name = topper_name;

-- Another way to assign and use window function
select name, branch, marks
from (select *,
first_value(name) over w as 'topper_name',
first_value(marks) over w as 'topper_marks'
from db.marks) as t
where marks = t.topper_marks and name = topper_name
window w as (partition by branch order by marks desc rows between unbounded preceding and unbounded following);

-- Lead and Lag window functions
select *,
lead(marks) over(order by marks desc),
lag(marks) over(order by marks asc)
from db.marks;

-- Calculating Cumulative Marks
SELECT *,
SUM(marks) OVER(PARTITION BY branch ORDER BY marks rows between unbounded preceding and current row)
FROM db.marks;

-- Calculating Cumulative Average
SELECT *,
AVG(marks) OVER(PARTITION BY branch ORDER BY marks rows between unbounded preceding and current row)
FROM db.marks;

-- Calculating the running average
SELECT *,
AVG(marks) OVER(PARTITION BY branch ORDER BY marks rows between 5 preceding and 0 following)
FROM db.marks;
-- A proper example would be - The average marks of a student in his recent 5 exams 

-- Calculating a pie chart
SELECT T.branch, MAX(T.percentage_marks)
FROM (SELECT *, SUM(marks) OVER (PARTITION BY branch) * 100 / SUM(marks) OVER() AS 'percentage_marks'
FROM db.marks) AS T
GROUP BY T.branch;

-- Calculating The Change in Views on Quarterly bases
SELECT YEAR(Date), QUARTER(Date), SUM(views) AS 'views',
((SUM(views) - LAG(SUM(views)) OVER(ORDER BY YEAR(Date),QUARTER(Date)))/LAG(SUM(views)) OVER(ORDER BY YEAR(Date),QUARTER(Date)))*100 AS 'Percent_change'
FROM youtube_views
GROUP BY YEAR(Date),QUARTER(Date)
ORDER BY YEAR(Date),QUARTER(Date);

-- Calculating a weekly percentage change
SELECT *,
((Views - LAG(Views, 7) OVER(ORDER BY Date))/LAG(Views,7) OVER(ORDER BY Date))*100 AS 'weekly_percent_change' -- 7th lag value
FROM youtube_views;

-- Percentiles and Quantiles
SELECT *,
((COUNT(name) OVER(ORDER BY marks ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) - 1) / COUNT(*) OVER()) * 100 AS 'percentile' -- Just replace 100 with 4 to calclulate Quartiles and simillarly for other varients
FROM db.marks;

-- Using Inbuilt Function - Getting an Error
SELECT 
    branch,
    marks,
    PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY marks) OVER (PARTITION BY branch) AS 'median_marks',
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY marks) OVER (PARTITION BY branch) AS 'median_marks_cont'
FROM db.marks;
-- Find and remove the outliers from the dataset using IQR formula and above function and methds

-- SEGMENTATION - Buckting the dataset
SELECT *,
NTILE(3) OVER(ORDER BY marks DESC) AS 'buckets'
FROM marks;

SELECT brand_name,model,price, 
CASE 
	WHEN bucket = 1 THEN 'budget'
    WHEN bucket = 2 THEN 'mid-range'
    WHEN bucket = 3 THEN 'premium'
END AS 'phone_type' -- Using case statement you are creating new column
FROM (SELECT brand_name,model,price,
NTILE(3) OVER(PARTITION BY brand_name ORDER BY price) AS 'bucket' 
FROM smartphones) t;

-- Cumulative Distribution
SELECT * FROM (SELECT *,
CUME_DIST() OVER(ORDER BY marks) AS 'Percentile_Score'
FROM marks) t;

SELECT * FROM (SELECT source,destination,airline,AVG(price) AS 'avg_fare',
DENSE_RANK() OVER(PARTITION BY source,destination ORDER BY AVG(price)) AS 'rank'
FROM flights
GROUP BY source,destination,airline) t
WHERE t.rank < 2