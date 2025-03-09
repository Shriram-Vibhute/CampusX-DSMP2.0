-- Creating View
create view view_1 as
select * from dml.smartphones
where brand_name = 'oneplus';

select * from view_1; -- A type of simple view

SET SQL_SAFE_UPDATES = False;

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