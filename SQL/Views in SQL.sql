-- Creating View
CREATE VIEW view1 AS (	
	SELECT * FROM dml.smartphones
	WHERE brand_name = 'oneplus'
);

SELECT * FROM view1; -- A type of simple view
SHOW TABLES; -- SQL considers views as tables

DROP VIEW view_1; -- dropping the view
-- All the operations on views are same just like physical tables

-- VIEWS and CTE's are kind of same but CTE's are temprary tables where views are perminant

SET SQL_SAFE_UPDATES = FALSE;

-- Complex View
CREATE VIEW joined_df AS (
	SELECT name, address, roll_no
	FROM T1
	INNER JOIN T2
	ON T1.user_id = T2.user_id
	INNER JOIN T3
	ON T2.roll_no = T3.roll_no
);

-- In views, you basically store the query instead of table and run it. (IMPORTANT)

-- Changing the data from main table will also get reflected in views. 
update dml.smartphones
set has_ir_blaster = true
where brand_name = 'oneplus';

select * from dml.smartphones;
select * from view_1; -- The changes are also reflected in view.

-- Changing the data from view will also get reflected in main table. 
update view_1
set has_nfc = true;

select * from dml.smartphones;
select * from view_1; -- The changes are also reflected in view.

-- Materilized Views - Present in Postgres and Oracle