-- Last updated: 8/20/2026, 2:02:51 AM
SELECT
    U.UNIQUE_ID AS 'unique_id',
    E.NAME AS 'name'
FROM
    EMPLOYEES E
LEFT JOIN
    EMPLOYEEUNI U
ON
    U.ID = E.ID;
