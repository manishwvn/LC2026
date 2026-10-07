-- Last updated: 10/7/2026, 2:56:59 PM
SELECT
    Q.ID AS 'id', 
    Q.YEAR AS 'year',
    IFNULL(N.NPV, 0) AS 'npv'
FROM
    QUERIES Q
LEFT JOIN
    NPV N
ON
    N.ID = Q.ID
    AND 
    N.YEAR = Q.YEAR
ORDER BY
    N.ID;
    