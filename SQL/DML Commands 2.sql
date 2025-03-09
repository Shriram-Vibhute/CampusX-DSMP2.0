CREATE DATABASE IF NOT EXISTS dml;
USE dml;

SELECT * FROM smartphones;

-- Calculating PPI
SELECT 
brand_name,
SQRT((resolution_width * resolution_width) + (resolution_height * resolution_height)) / screen_size AS  'ppi'
FROM smartphones;

-- Creating new column with default values
SELECT
brand_name, 'smartphone' AS 'phone'
from smartphones;

-- Fetching unique values
SELECT DISTINCT (brand_name) from smartphones;
-- Fetching unique combination of columns
SELECT DISTINCT brand_name, processor_brand from smartphones; -- There are no brackets unless you mention only one column

SELECT * FROM smartphones
WHERE brand_name IN ('oneplus', 'samsung', 'motorola');

-- update operation
UPDATE smartphones
SET brand_name = 'Oneplus', num_cores = 10 -- updating more than column values
WHERE brand_name = 'oneplus'; -- where condition is important otherwise all values will get updated

DELETE FROM smartphones
WHERE brand_name = 'oneplus', num_cores = 8; -- make sure to mention where consition otherwise entire data will get deleted

-- DELETE and UPDATE are perminant Querries