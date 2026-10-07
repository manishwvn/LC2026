-- Last updated: 10/7/2026, 2:44:53 PM
# Please, upvote if you like it. Thanks :-)
SELECT e1.employee_id,
       COUNT(*) AS overlapping_shifts
FROM EmployeeShifts e1 JOIN EmployeeShifts e2
ON e1.employee_id=e2.employee_id
WHERE e1.start_time < e2.start_time AND e1.end_time > e2.start_time
GROUP BY e1.employee_id
ORDER BY employee_id