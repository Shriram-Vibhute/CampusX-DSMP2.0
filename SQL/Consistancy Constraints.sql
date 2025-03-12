-- Constraints
-- 1. NOT NULL
-- 2. UNIQUE(combo)
-- 		Another way of creating constraint
-- 3. PRIMARY KEY
-- 4. AUTO INCREMENT
-- 5. CHECK
-- 6. DEFAULT
-- 7. FOREIGN KEY
USE db;
CREATE TABLE joining_table(
	roll_no INT PRIMARY KEY 
    -- If this key is a foreign key in another table then here in the independent table the corrosponding column must be a primary key or have a unique constraint
);
INSERT INTO joining_table VALUES (1);

CREATE TABLE constraints(
	id INT PRIMARY KEY AUTO_INCREMENT, -- You dont need to pass the value of this columns, Since this is a Auto-Increment column you have to insert values into this table by explicit columns mentioning.
    registeration_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- If user didnt provided value to this column then default value will be inserted at this place
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    roll_no INT,
    age INT CHECK (age > 18 AND age < 50), -- For comparing with different values, you can only use (<, >, =, !) operator
    
    -- Mentioning Constraints
    CONSTRAINT db_constraints_unique UNIQUE (email), # The pattern of name - db_constraints_unique (db_name table_name constraint) is an industrial nomeenclature
    -- whats an advatage of this complex form of assigning constraints - 
    CONSTRAINT db_constraints_unique_2 UNIQUE (email, name), -- 1. You can combine more than one columns into one constraint
    -- 2. You can delete this perticular constrainet since we provided the name to it.
    CONSTRAINT db_constraint_foreign_key FOREIGN KEY (roll_no) REFERENCES joining_table (roll_no) -- 3. This is the only way to mention FOREIGN KEY
);

INSERT INTO constraints values (
	1,	-- id
	NOW(), -- registeration_date
    'dexter', -- name
    'dexter@gmail.com', -- email
    1, -- roll_no - The value that you are inserting into a dependent table (table have foreign key) must be present in independent table
    23 -- age
);
SELECT * FROM constraints;
-- Refrential Actions - What is the effect of updating or deleting date from one table (Primary Key) on another table (Foreign Key)
-- 1. RESTRICT (default) - If simply throws an error. Does not allow to make any changes
-- 2. CASCADE - The changes releted to that perticular columns will be reflected to all the similar columns of another column
-- 3. SET NULL - If you delete a record from one table then all the records releted to that record in other table will set to NULL
-- 4. SET DEFAULT - If you delete a record from one table then all the records releted to that record in other table will set to DEFAULT value passed
CREATE TABLE joining_refrential_actions(
	name VARCHAR(255) UNIQUE NOT NULL
);
INSERT INTO joining_refrential_actions VALUES
('default'), ('a'), ('b'), ('c');

CREATE TABLE refrential_actions(
	id INT PRIMARY KEY,
    name VARCHAR(255) DEFAULT "default",
    
    CONSTRAINT db_refrential_actions_foreign_key FOREIGN KEY (name) REFERENCES joining_refrential_actions (name)
    -- ON DELETE CASCADE -- Thats how you mention
-- 	ON UPDATE CASCADE
    
    -- ON DELETE SET NULL
    -- ON UPDATE SET NULL
    
    -- error
    ON DELETE SET DEFAULT  -- Set the default value of 'name' column when the referenced row is deleted
    ON UPDATE SET DEFAULT  -- Set the default value of 'name' column when the referenced row is updated
    -- If there are multiple columns acting as foreign key then you have to mention this above lines every time you working with those columns
);
INSERT INTO refrential_actions VALUES
(1, 'a'), (2, 'a'), (3, 'a');

DELETE FROM joining_refrential_actions
WHERE name = 'a';
SELECT * FROM refrential_actions; -- The records havning name = 'a' present in the dependent table will get deleted

-- SQL databases (including SQLite, MySQL before version 8.0.20, and others) do not implement this specific behavior -- only SET DEFAULT action.