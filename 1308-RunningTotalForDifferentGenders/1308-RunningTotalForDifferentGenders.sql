-- Last updated: 10/7/2026, 2:58:23 PM
SELECT gender, day, sum(score_points) over (partition by gender order by gender, day) as total
FROM Scores