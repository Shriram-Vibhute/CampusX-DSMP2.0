use db;
create table users(
	id int primary key auto_increment,
    name varchar(255),
    email varchar(255)
);

insert into users values
(1, 'tejas', 'tejas@gmail.com');
select * from users;

-- Creating a Stored Procedure - Insert a new user into the database if email of that user is not already present in it
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_user`(
	IN input_name VARCHAR(255), -- IN -> Input
    IN input_email VARCHAR(255), -- OUT -> Return
    OUT message VARCHAR(255) -- This variable will automatically get returned at the end of the function
)
BEGIN
	DECLARE counter INTEGER;
    SELECT COUNT(*) INTO counter FROM db.users -- `COUNT(*) INTO counter` -> is a another way to assign value into counter
    WHERE email = input_email;
    
    -- Conditions
    IF counter = 0 THEN
		INSERT INTO db.users(name, email) VALUES (input_name, input_email);
        SET message = "User Created Successfully";
	ELSE
		SET message = "Sorry, Email already exists";
	END IF;
END

SET @message = '';
CALL new_user("sanket", "sanket@gmail.com", @message);
SELECT @message; -- The message is not updating, Why?

-- Remaining