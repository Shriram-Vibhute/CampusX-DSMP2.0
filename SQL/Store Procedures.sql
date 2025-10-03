USE db;
CREATE TABLE IF NOT EXISTS users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    NAME VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO users VALUES
(1, 'tejas', 'tejas@gmail.com');
SELECT * FROM users;

-- Creating a Stored Procedure - Insert a new user into the database if email of that user is not already present in it
SET @message = "";
CALL new_user('tejas', 'tejas@gmail.com', @message);
SELECT @message;

SET @message = "";
CALL new_user('sanket', 'sanket@gmail.com', @message);
SELECT @message;