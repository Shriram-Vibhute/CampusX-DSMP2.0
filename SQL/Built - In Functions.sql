CREATE TABLE sample_data (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    score DECIMAL(5,2),
    salary DECIMAL(10,2),
    age INT,
    created_at TIMESTAMP
);

-- Insert some sample data
INSERT INTO sample_data (id, name, score, salary, age, created_at)
VALUES
    (1, 'Alice', 85.50, 50000.00, 25, '2023-01-01 00:00:00'),
    (2, 'Bob', 90.00, 60000.00, 30, '2023-01-02 00:00:00'),
    (3, 'Carol', 78.00, 55000.00, 28, '2023-01-03 00:00:00'),
    (4, 'David', 92.00, 70000.00, 32, '2023-01-04 00:00:00'),
    (5, 'Emma', 88.00, 58000.00, 29, '2023-01-05 00:00:00');

SELECT 
    MAX(score) AS max_score,
    MIN(score) AS min_score,
    COUNT(*) AS total_records,
    SUM(salary) AS total_salary,
    AVG(score) AS avg_score,
    STDDEV(score) AS std_dev_score,
    VARIANCE(score) AS variance_score
FROM sample_data;

SELECT 
    name,
    score,
    ABS(score - 90) AS score_diff_from_90,
    ROUND(score, 0) AS rounded_score,
    CEIL(score) AS ceiling_score,
    FLOOR(score) AS floor_score,
    SQRT(score) AS sqrt_score
FROM sample_data;

-- Fetching unique values
SELECT DISTINCT (brand_name) from smartphones;
-- Fetching unique combination of columns
SELECT DISTINCT brand_name, processor_brand from smartphones; -- There are no brackets unless you mention only one column