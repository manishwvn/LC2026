-- Last updated: 8/20/2026, 1:56:40 AM
# Write your MySQL query statement below
SELECT student_id, department_id, 
    ROUND(100*PERCENT_RANK() OVER (
          PARTITION BY department_id 
          ORDER BY mark DESC)
    , 2) AS percentage 
FROM Students