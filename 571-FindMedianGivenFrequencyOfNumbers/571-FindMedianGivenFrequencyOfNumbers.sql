-- Last updated: 8/20/2026, 2:11:21 AM
# Write your MySQL query statement below
SELECT 
	AVG(num) AS median
FROM (
SELECT 
		*,
		SUM(frequency)OVER(ORDER BY num) AS cum1,
        SUM(frequency)OVER(ORDER BY num DESC) AS cum2,
		SUM(frequency)OVER() AS Tot
	FROM numbers
	) t
WHERE  cum1 >= tot/2 AND cum2 >= tot/2