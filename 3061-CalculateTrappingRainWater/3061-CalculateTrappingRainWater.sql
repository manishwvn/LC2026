-- Last updated: 10/7/2026, 2:45:46 PM
WITH CTE AS (
    SELECT *,
        MAX(height) OVER(ORDER BY id ASC) AS left_highest_bar,
        MAX(height) OVER(ORDER BY id DESC) AS right_highest_bar
    FROM Heights
)
SELECT 
    SUM(LEAST(left_highest_bar, right_highest_bar) - height) AS total_trapped_water 
FROM CTE

