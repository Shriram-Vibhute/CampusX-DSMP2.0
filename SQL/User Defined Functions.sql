-- Function Executioncounter_brand
CREATE DEFINER=`root`@`localhost` FUNCTION `hello_world`() RETURNS varchar(255) CHARSET utf8mb4
    DETERMINISTIC
BEGIN
-- Since your function does not modify data and only returns a constant string, you can use DETERMINISTIC or NO SQL.
	RETURN "hello_world";
END

SELECT hello_world();
SELECT hello_world() FROM db.marks; -- Executes no. rows times

-- Parameterized Function

CREATE DEFINER=`root`@`localhost` FUNCTION `find_age`(
	date_of_birth DATE
) RETURNS int
    DETERMINISTIC
BEGIN
	-- If you pass the Date of birth then this function will return the age of that person
    DECLARE age INTEGER;
    SET age = ROUND(DATEDIFF(NOW(), date_of_birth) / 365);
    RETURN age;
END

SELECT find_age(DATE('2020-5-12'));
-- Throwing an erro while passing a DATETIME instead you can you STR_TO_DATE function to pass DATETIME

-- Conditional Function

CREATE DEFINER=`root`@`localhost` FUNCTION `create_name`(
	name VARCHAR(255),
    gender VARCHAR(1),
    married BOOL
) RETURNS varchar(255) CHARSET utf8mb4
    DETERMINISTIC
BEGIN
	DECLARE new_name VARCHAR(255);
    IF gender = 'M' THEN
		SET new_name = CONCAT('Mr ', name);
	ELSE
		IF gender = 'F' AND married = TRUE THEN
			SET new_name = CONCAT('Mrs ', name);
		ELSE
			SET new_name = CONCAT('Ms ', name);
		END IF;
	END IF;
RETURN new_name;
END

SELECT create_name("DEXTER", 'M', TRUE), create_name("GWEN", 'F', FALSE), create_name("SARA", 'F', TRUE);

-- You can also return a value directly by returning a query

CREATE DEFINER=`root`@`localhost` FUNCTION `counter_brand`(brand VARCHAR(255)) RETURNS int
    DETERMINISTIC
BEGIN
	RETURN (SELECT COUNT(*) FROM dml.smartphones WHERE brand_name = brand);
END

SELECT counter_brand('oneplus');

-- You cannot return more than one values form a function