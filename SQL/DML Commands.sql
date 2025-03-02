-- Data Manipulation Languages (DML) Commands

CREATE TABLE IF NOT EXISTS dml_commands(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    branch VARCHAR(255) NOT NULL
);

-- INSERT
INSERT INTO dml_commands() 
VALUES (1, 'jonny', 'IT'), (2, 'DEX', 'CS'), (3, 'SAM', 'MEAH');

-- DELETE
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dml_commands
WHERE name = 'DEX';

-- UPDATE
UPDATE dml_commands
SET name = 'new_name', branch = 'ABC'
WHERE id = 1;

SELECT * FROM dml_commands;