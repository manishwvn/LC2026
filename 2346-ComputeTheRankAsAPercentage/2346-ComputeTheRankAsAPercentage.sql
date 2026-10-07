-- Last updated: 10/7/2026, 2:49:12 PM
# Write your MySQL query statement below
SELECT student_id, department_id, 
    ROUND(100*PERCENT_RANK() OVER (
          PARTITION BY department_id 
          ORDER BY mark DESC)
    , 2) AS percentage 
FROM Students