# Write your MySQL query statement below

SELECT World.name, World.population, World.area
FROM World
WHERE World.area >= 3000000 OR World.population >= 25000000;