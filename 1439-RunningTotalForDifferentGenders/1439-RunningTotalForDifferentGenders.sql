-- Last updated: 8/20/2026, 2:03:34 AM
SELECT gender, day, sum(score_points) over (partition by gender order by gender, day) as total
FROM Scores