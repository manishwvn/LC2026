-- Last updated: 10/7/2026, 2:52:23 PM
SELECT t.employee_id
FROM (
    SELECT e.employee_id, e.name, s.salary
    FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    UNION
    SELECT s.employee_id, e.name, s.salary
    FROM Employees e
    RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
) AS t
WHERE t.name IS NULL OR t.salary IS NULL
ORDER BY t.employee_id;