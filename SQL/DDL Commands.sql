CREATE DATABASE IF NOT EXISTS db; -- Exists is a clause used with only databases and tables to check whether they exists or not
USE db;

-- EXISTS Clause : The SQL EXISTS clause is primarily used to filter rows based on the existence of related records in another table or to enforce conditional logic in subqueries
SELECT order_id 
FROM orders 
WHERE EXISTS (
  SELECT 1 FROM order_items -- Return all the columns
  WHERE orders.order_id = order_items.order_id
);

CREATE DATABASE practice;
CREATE TABLE tb(
	col INT
);
INSERT INTO tb VALUES (1), (2), (3), (4), (5);
SELECT * FROM  practice.tb
WHERE EXISTS (
	SELECT * FROM practice.tb
    WHERE col = col
); -- If subquerry return data then the main querry will return as well

SELECT * FROM  practice.tb
WHERE NOT EXISTS (
	SELECT * FROM practice.tb
    WHERE col = col
); -- In this case, subquerry returns rows but since we are using NOT EXISTS this will chenge TRUE -> FALSE thats why main querry remains empty

-- ----------------------------------------------------------------------------------------------------------------
-- STRING DATATYPES
CREATE TABLE IF NOT EXISTS string_datatypes(
	col1 CHAR(255), -- Static - 0 to 255. Default is 1
    col2 VARCHAR(255), -- Dynamic - can be from 0 to 65535
    col3 TEXT, -- maximum length of 65,535 bytes
    col4 MEDIUMTEXT, -- maximum length of 16,777,215 characters
    col4 LONGTEXT -- maximum length of 4,294,967,295 characters
    -- The "BINARY" and "BLOB - binary large object" comes under string datatypes
);

-- NUMERIC DATATYPES
CREATE TABLE IF NOT EXISTS numeric_datatypes(
	-- Numeric Datatypes
    id INT, -- -2^31 to 2^31 - 1
    age SMALLINT, -- -2^15 to 2^15 - 1
    phone BIGINT, -- -2^63 to 2^63 - 1
    new_column TINYINT, -- 0 to 255 
    
    -- Flotting point Numbers
    height FLOAT(10), -- FLOAT(p) -> MySQL uses the p value to determine whether to use FLOAT or DOUBLE for the resulting data type. If p is from 0 to 24, the data type becomes FLOAT(). If p is from 25 to 53, the data type becomes DOUBLE()
    weight REAL,
    
    -- Formatted Numbers -> The numbers which are relatively bigger than INT
    num_1 DECIMAL(5, 3), -- The total number of digits is specified in first number and the number of digits after the decimal point is specified in the second parameter. The maximum number for size is 65. The maximum number for d is 30. The default value for size is 10.
    num_2 NUMERIC(6, 3)
);

-- BOOLEAN DATATYPES
CREATE TABLE IF NOT EXISTS boolean_datatypes(
	col BOOLEAN
);

-- DATETIME DATATYPES
CREATE TABLE IF NOT EXISTS datetime_datatypes(
	birth_date DATE, -- Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
    birth_time TIME, -- Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'
    today_time DATETIME, -- Format: YYYY-MM-DD hh:mm:ss.
    curr_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time
    time_col_second TIMESTAMP, -- Format: hh:mm:ss. TIMESTAMP values are stored as the number of seconds
    yr YEAR -- Format: YYYY.
);

INSERT INTO datatypes VALUES (1, 43, 123456, 1, 5.11, 50, 12.123, 123.123, 'Dexter', 'India', False, '2000-10-23', '05:34:50', '2000-10-23 05:34:50');
SELECT * FROM datatypes;

-- Data Defination Language(DDL) Commands 🎯
SHOW TABLES; -- to see all tables in a selected databases

-- 1. DESCRIBE
DESCRIBE datatypes; -- another way "DESC TABLE datatypes" - Return the type of columns, null values and type of key

-- 2. CREATE -> DATABASE, TABLE
CREATE DATABASE IF NOT EXISTS bd;
CREATE TABLE IF NOT EXISTS tb(name VARCHAR(255) NOT NULL);

-- 3. ALTER -> ADD, MODIFY, DROP
ALTER TABLE datatypes
ADD new_column_1 INT NOT NULL DEFAULT 10; -- Initially all values in the columns are initialized to 0.

ALTER TABLE datatypes
MODIFY new_column_1 VARCHAR(255); -- You cannot change the datatype from string to decimal.

ALTER TABLE datatypes
ADD new_column_2 INT; -- But you can change from int to string, infact you can change anything to string

ALTER TABLE datatypes
DROP new_column_2;

-- 4. DROP -> Database, Table
DROP TABLE IF EXISTS tb;
DROP DATABASE IF EXISTS db;

-- 5. RENAME
RENAME TABLE datatypes TO new_datatypes;

-- 6. TRUNCATE
TRUNCATE TABLE new_datatypes;
SELECT * FROM new_datatypes;

-- Difference between trucate and drop -> drop will removes the entire data with table but truncate will only deletes the data
-- Note: All the numeric data types may have an extra option: UNSIGNED or ZEROFILL. If you add the UNSIGNED option, MySQL disallows negative values for the column. If you add the ZEROFILL option, MySQL automatically also adds the UNSIGNED attribute to the column.