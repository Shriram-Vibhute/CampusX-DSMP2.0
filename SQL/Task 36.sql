-- 1: What are the top 5 patients who claimed the highest insurance amounts?
SELECT *, ROW_NUMBER() OVER(ORDER BY claim) FROM db.insurance LIMIT 5;

-- 2: What is the average insurance claimed by patients based on the number of children they have?
SELECT * FROM (SELECT *,
AVG(claim) OVER(PARTITION BY children) AS avg_claim,
ROW_NUMBER() OVER(PARTITION BY children ORDER BY claim ASC) AS row_num
FROM db.insurance) AS T
WHERE T.row_num = 1;

-- 3: What is the highest and lowest claimed amount by patients in each region?
SELECT *,
MAX(claim) OVER(PARTITION BY region),
MIN(claim) OVER(PARTITION BY region)
FROM db.insurance;

-- 4: What is the percentage of smokers in each age group?
SELECT *,
COUNT(*) OVER(PARTITION BY age) / COUNT(*) OVER() -- Consider an entire dataset as a single window
FROM db.insurance;

-- 5: What is the difference between the claimed amount of each patient and the patient who claimed first?
SELECT *,
claim - FIRST_VALUE(claim) OVER() AS diff
FROM db.insurance;

-- 6: For each patient, calculate the difference between their claimed amount and the average claimed amount of patients with the same number of children.
SELECT *,
claim - AVG(claim) OVER(PARTITION BY children)
FROM db.insurance;

-- 7: Show the patient with the highest BMI in each region and their respective rank.
SELECT * FROM db.insurance
WHERE (region, BMI) IN (SELECT region, MAX(bmi) AS BMI FROM db.insurance
GROUP BY region); -- Brute Force

SELECT * FROM (SELECT *,
RANK() OVER(PARTITION BY region ORDER BY bmi DESC) AS group_rank
FROM insurance) t
WHERE t.group_rank = 1;

-- 8: Calculate the difference between the claimed amount of each patient and the claimed amount of the patient who has the highest BMI in their region.
SELECT t1.claim - t2.claim FROM (
	SELECT * FROM (SELECT *,
	RANK() OVER(PARTITION BY region ORDER BY bmi DESC) AS group_rank
	FROM insurance) t
	WHERE t.group_rank = 1
) AS t1, db.insurance AS t2
WHERE t1.region = t2.region;

SELECT *,
claim - FIRST_VALUE(claim) OVER(PARTITION BY region ORDER BY bmi DESC)
FROM insurance;

-- 9: For each patient, calculate the difference in claim amount between the patient and the patient with the highest claim amount among patients with the same bmi and smoker status, within the same region. Return the result in descending order difference.
SELECT *,
claim - MAX(claim) OVER(PARTITION BY bmi, smoker, region)
FROM insurance;

-- 10: For each patient, find the maximum BMI value among their next three records (ordered by age).
SELECT *,
MAX(bmi) OVER(ORDER BY age ROWS BETWEEN 0 PRECEDING AND 3 FOLLOWING)
FROM insurance;

-- 11: For each patient, find the rolling average of the last 2 claims.
SELECT *,
AVG(claim) OVER(ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING) -- Interesting Question
FROM insurance;

-- 12: Find the first claimed insurance value for male and female patients, within each region order the data by patient age in ascending order, and only include patients who are non-diabetic and have a bmi value between 25 and 30.
SELECT * FROM (
	SELECT *,
	FIRST_VALUE(claim) OVER(PARTITION BY gender, region ORDER BY age) AS f_val,
	ROW_NUMBER() OVER(PARTITION BY gender, region ORDER BY age) AS row_no
	FROM db.insurance
    WHERE diabetic = 'No' AND bmi BETWEEN 25 AND 30
) AS T
WHERE T.row_no = 1;