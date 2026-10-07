-- Last updated: 10/7/2026, 2:47:07 PM
with cte as (SELECT *,
ROUND(1/COUNT(voter)OVER(PARTITION BY voter),2) as points
FROM Votes
WHERE candidate IS NOT NULL
),
cte1 as(
SELECT voter, candidate, RANK()OVER(ORDER BY SUM(points) DESC) as rn
FROM cte
GROUP BY 2)

SELECT candidate
FROM cte1
where rn = 1 order by 1;