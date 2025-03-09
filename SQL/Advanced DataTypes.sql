use db;
-- Numeric Datatypes
create table numeric_datatypes(
	-- integer datatypes
	id int primary key,
    age tinyint,
    weight smallint,
    likes mediumint signed,
    views bigint unsigned,
    
    -- Decimal Datatypes
    height decimal(5, 2), -- If you store the number which have more than 2 numbers after decimal point it will get round of.
    d_type_float float, -- range of 7 numbers
    d_type_double double -- range of 15 numbers
);

insert into numeric_datatypes values
(1, 23, 155,32444, 77234896, 23.855, 56.0986545, 34555.09781245090);
select * from numeric_datatypes; -- You can see the decimal values are rounded of.

-- Remaining String DataTypes
create table string_datatypes(
	gender enum('male', 'female'),
    hobbies set('playing', 'reading', 'singing', 'dancing')
);
insert into string_datatypes values
('others', 'drawing'), -- Empty string inserted
('male', 'playing,reading'); -- Cannot insert like this - 'playing, reading'
select * from string_datatypes;

-- Other Datatypes
-- blob
create table other_datatypes_1(
	dp mediumblob not null -- adding display profile
);
insert into other_datatypes_1(dp) values
(load_file("C:/Users/shrir/OneDrive/Pictures/Screenshots/Screenshot 2025-03-06 105613.png"));
select * from other_datatypes_1;

-- geometry - points, lines and polygon
create table other_datatypes_2(
	latlong geometry -- adding display profile
);
insert into other_datatypes_2(latlong) values
(point(123.4, 675.9));
select st_astext(latlong), st_x(latlong), st_y(latlong) from other_datatypes_2; -- convert blog to text representation

-- json
create table other_datatypes_3(
	description json -- adding display profile
);
insert into other_datatypes_3 (description) values 
('{
	"name": "dexter",
	"desc": "ML Engineer"
}');
select description, json_extract(description, '$.desc') from other_datatypes_3;