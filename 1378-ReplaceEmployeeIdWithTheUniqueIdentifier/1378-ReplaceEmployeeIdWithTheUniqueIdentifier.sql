-- Last updated: 10/7/2026, 2:57:26 PM
SELECT
    U.UNIQUE_ID AS 'unique_id',
    E.NAME AS 'name'
FROM
    EMPLOYEES E
LEFT JOIN
    EMPLOYEEUNI U
ON
    U.ID = E.ID;
