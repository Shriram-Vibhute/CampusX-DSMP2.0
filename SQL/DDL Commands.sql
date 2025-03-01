CREATE DATABASE IF NOT EXISTS db;
USE db;

-- DATATYPES IN SQL
CREATE TABLE IF NOT EXISTS datatypes(
	-- Numeric Datatypes
    id SMALLINT, -- -2^31 to 2^31 - 1
    age INT, -- -2^15 to 2^15 - 1
    phone BIGINT, -- -2^63 to 2^63 - 1
    new_column TINYINT, -- 0 to 255 
    
    -- Flotting point Numbers
    height FLOAT(10),
    weight REAL,
    
    -- Formatted Numbers -> The numbers which are relatively bigger than INT
    num_1 DECIMAL(5, 3),
    num_2 NUMERIC(6, 3),
    
    -- Character string type
    name CHAR(255),
    address VARCHAR(255),
    
    -- Boolean
    married BOOLEAN,
    
    -- DATE TIME
    birth_date DATE,
    birth_time TIME,
    today_time DATETIME
);

INSERT INTO datatypes VALUES (1, 43, 123456, 1, 5.11, 50, 12.123, 123.123, 'Dexter', 'India', False, '2000-10-23', '05:34:50', '2000-10-23 05:34:50');
SELECT * FROM datatypes;

-- Data Defination Langiage(DDL) Commands 🎯
SHOW TABLES; -- to see all tables in a selected databases

-- 1. DESCRIBE
DESCRIBE datatypes; -- another way "DESC TABLE datatypes" - Return the type of columns, null values and type of key

-- 2. CREATE -> DATABASE, TABLE
CREATE DATABASE IF NOT EXISTS bd;
CREATE TABLE IF NOT EXISTS tb(name VARCHAR(255) NOT NULL);

-- 3. ALTER -> ADD, MODIFY, DROP
ALTER TABLE datatypes
ADD new_column_1 INT NOT NULL; -- Initially all values in the columns are initialized to 0.

ALTER TABLE datatypes
MODIFY new_column_1 NUMERIC(2,2);

ALTER TABLE datatypes
ADD new_column_2 INT;

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

-- Constraints
-- 1. NOT NULL
-- 2. UNIQUE(combo)
-- 		Another way of creating constraint
-- 3. PRIMARY KEY
-- 4. AUTO INCREMENT
-- 5. CHECK
-- 6. DEFAULT
-- 7. FOREIGN KEY

CREATE TABLE constraints_2(
	roll_no INT PRIMARY KEY -- If this key is a foreign key in another table then here in the independent table the corrosponding column must be a primary key or have a unique constraint
);
DROP TABLE constraints;
CREATE TABLE constraints(
	id INT PRIMARY KEY AUTO_INCREMENT,
    registeration_date DATETIME DEFAULT CURRENT_TIMESTAMP, # If user didnt provided value to this column then default value will be inserted at this place
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    roll_no INT, -- While you are inserting all values in the table you dont need to pass the value of this column
    age INT CHECK (age > 18 AND age < 50), -- For comparing with different values
    
    -- Mentioning Constraints
    CONSTRAINT db_constraints_unique UNIQUE (email), # The pattern of name - db_constraints_unique (db_name table_name constraint) is an industrial nomeenclature
    -- whats an advatage of this complex form of assigning constraints - 
    CONSTRAINT db_constraints_unique_2 UNIQUE (email, name), -- 1. You can combine more than one columns into one constraint
    -- 2. You can delete this perticular constrainet since we provided the name to it.
    CONSTRAINT db_constraint_foreign_key FOREIGN KEY (roll_no) REFERENCES constraints_2 (roll_no) -- 3. This is the only way to mention FOREIGN KEY
);

INSERT INTO constraints values (
	1,	
	NOW(),
    'dexter',
    'dexter@gmail.com',
    1,
    23
);
SELECT * FROM constraints;

-- Refrential Actions - What is the effect of updating or deleting date from one table (Primary Key) on another table (Foreign Key)
-- 1. RESTRICT (default) - If simply throws an error. Does not allow to make any changes
-- 2. CASCADE - The changes releted to that perticular columns will be reflected to all the similar columns of another column
-- 3. SET NULL - If you delete a record from one table then all the records releted to that record in other table will set to NULL
-- 4. SET DEFAULT - If you delete a record from one table then all the records releted to that record in other table will set to DEFAULT value passed

CREATE TABLE refrential_actions(
	id INT PRIMARY KEY,
    name VARCHAR(255),
    
    CONSTRAINT db_refrential_actions_foreign_key FOREIGN KEY (name) REFERENCES refrential_actions2 (name)
    ON DELETE CASCADE -- Thats how you mention
	ON UPDATE CASCADE
    
    -- ON DELETE SET NULL
    -- ON UPDATE SET NULL
    
    -- error
    -- ON DELETE SET DEFAULT  -- Set the default value of 'name' column when the referenced row is deleted
    -- ON UPDATE SET DEFAULT  -- Set the default value of 'name' column when the referenced row is updated
    -- If there are multiple columns acting as foreign key then you have to mention this above lines every time you working with those columns
);
