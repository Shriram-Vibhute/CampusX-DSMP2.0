USE dml;
CREATE TABLE uber_rides(
	ride_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    cab_id INT,
    start_time DATETIME,
    end_time DATETIME
);
INSERT INTO uber_rides (user_id, cab_id, start_time, end_time)
VALUE (1, 1, '2025-03-09 08:00:00', '2025-03-09 09:00:00'),
(2, 2, '2025-09-04 15:00:00', '2025-09-04 15:30:00'),
(3, 3, '2023-10-10 01:00:00', '2025-10-10 08:00:00'),
(4, 4, '2024-01-21 05:00:00', '2025-01-21 18:00:00'),
(5, 5, '2022-03-09 08:00:00', '2025-03-09 09:00:00'); -- DateTime has to be inserted in the form of strings.
SELECT * FROM uber_rides;

-- DateTime Functions
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT NOW();
-- It will show the current time of the server on which your database is stored,

-- DateTime Extraction Functions
SELECT
DATE(start_time), -- complete date - YYYY-MM-DD
TIME(start_time), -- complete time - HH:MM:SS
YEAR(start_time), -- year - YYYY
MONTH(start_time), -- month - MM
MONTHNAME(start_time), -- monthname - str
DAY(start_time), -- day - integer
DAYNAME(start_time), -- dayname - str
HOUR(start_time), -- hour - HH
MINUTE(start_time), -- minute - MM
SECOND(start_time), -- second - SS
DAYOFYEAR(start_time), DAYOFMONTH(start_time), DAYOFWEEK(start_time), -- integer
QUARTER(start_time), -- int
WEEK(start_time), WEEKOFYEAR(start_time), -- Both are same - int
LAST_DAY(start_time) -- Last day in an corrosponding month
FROM uber_rides;

-- DateTime Formatting
SELECT start_time, DATE_FORMAT(start_time, "%d %b %y") -- %b - month name
FROM uber_rides;

SELECT start_time, TIME_FORMAT(start_time, '%l:%i %p')
FROM uber_rides;

WITH T AS (
	SELECT start_time, TIME_FORMAT(start_time, '%l:%i %p') AS "time_format"
	FROM uber_rides
)
SELECT HOUR(time_format) FROM T; 

-- Time Conversion
-- Implicit
SELECT '2020-8-12' > '2020-8-13', '2020-8-12' > DATE_FORMAT('2020-8-13', "%d %b %y"); -- In first comparison the implicit conversion takes place but not in 2nd comparision

-- Explicit
SELECT STR_TO_DATE('13 AUG 2020', '%e %b %y');

-- DateTime Arithmetic
SELECT DATEDIFF(end_time, start_time), TIMEDIFF(end_time, start_time) FROM uber_rides;

-- add/sub without extracting perticular part of datetime
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 DAY);
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 MONTH);
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 YEAR);
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 QUARTER);

SELECT DATE_SUB(CURRENT_DATE(), INTERVAL 10 DAY);

-- ADDTIME and SUBTIME - Addition and Subtraction of two times
SELECT ADDDATE(CURRENT_DATE(), "22-07-2026"); -- Adding days only
SELECT ADDTIME(CURRENT_TIME(), "10:00:00"); -- It will exceed beyond 24hrs

-- Auto-Update Feature in Timestamp
CREATE TABLE auto_update(
	id INT PRIMARY KEY,
	t TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO auto_update values (2,CURRENT_TIMESTAMP);
SELECT * FROM auto_update;

UPDATE auto_update
SET id = 3
WHERE id = 2; -- If you update here the corrosponding DateTime will also get updated.