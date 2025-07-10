-- Top 5 highest screen size smasung phones
SELECT brand_name, screen_size
FROM dml.smartphones
WHERE brand_name = 'samsung'
ORDER BY screen_size DESC
LIMIT 5;

-- Sort the dataset on the bases of ppi
SELECT brand_name, 
ROUND(SQRT((resolution_height * resolution_height) + (resolution_width * resolution_width)) / screen_size) AS 'ppi'
FROM dml.smartphones
ORDER BY ppi DESC
LIMIT 5;

-- Find the phone who have 2nd largest battery - (IMP)
SELECT brand_name, model, battery_capacity FROM dml.smartphones
ORDER BY battery_capacity DESC
LIMIT 1, 1; -- Starting from 1st index (zero based indexing) and from that return first 1 records;

-- Find the name and rating of worst rated apple phone
SELECT model, rating
FROM dml.smartphones
WHERE brand_name = 'apple'
ORDER BY rating ASC
LIMIT 0, 1;

-- Sort the phones alphabetically and then on the bases of rating in descending order
SELECT *
FROM dml.smartphones
ORDER BY brand_name ASC, rating DESC;

-- Group smartphones by brand and get the count, avg price, max rating, avg screen size and avg battery capacity
SELECT COUNT(*), AVG(price), MAX(rating), AVG(screen_size), AVG(battery_capacity)
FROM dml.smartphones
GROUP BY brand_name; -- GROUP BY in SQL does make a group of NULL values if there is null values which you applied group by.

-- groupby using has_nfc and find avg_rating
SELECT has_nfc, AVG(price), AVG(rating)
FROM dml.smartphones
GROUP BY has_nfc;

-- Group smartphones by the brand_name and processor_brand and get the count of models and the avg primary_camera_front_resolution
SELECT brand_name, processor_brand, COUNT(*), AVG(primary_camera_front)
FROM dml.smartphones
GROUP BY brand_name, processor_brand; -- groupby on 2 columns

-- Find top 5 most costly phone brands
SELECT brand_name, MAX(price) AS 'max_price'
FROM dml.smartphones
GROUP BY brand_name
ORDER BY max_price
LIMIT 5;

-- avg price of 5G phones vs avg_price of non-5G phones
SELECT has_5g, AVG(price)
FROM dml.smartphones
GROUP BY has_5g;

-- Find all samsung 5G enabled phones and find out the avg price of those have NFC and those have dont.
SELECT has_nfc, AVG(price)
FROM dml.smartphones
WHERE has_5g = 'True' AND brand_name = 'samsung'
GROUP BY has_nfc;

-- Find the avg price of smartphones which have more than 20 phones
SELECT brand_name, AVG(price) AS avg_price
FROM dml.smartphones
GROUP BY brand_name
HAVING COUNT(*) > 20;

-- Find the top 3 brands with the highest avg refresh rate of atleast 90HZ and fast charging is available and dont consider brands which have less than 10 phones
SELECT brand_name, AVG(refresh_rate) AS avg_refresh_rate 
FROM dml.smartphones
WHERE fast_charging IS NOT NULL -- WHERE fast_charging != NULL (is wrong querry) 
GROUP BY (brand_name)
HAVING avg_refresh_rate >= 90 AND COUNT(*) > 10
ORDER BY avg_refresh_rate
LIMIT 3;