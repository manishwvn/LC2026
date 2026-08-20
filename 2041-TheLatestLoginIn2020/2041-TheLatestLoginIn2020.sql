-- Last updated: 8/20/2026, 1:59:28 AM
SELECT 
    USER_ID AS 'user_id',
    MAX(TIME_STAMP) AS 'last_stamp'
FROM 
    LOGINS
WHERE
    YEAR(TIME_STAMP) = '2020'
GROUP BY
    USER_ID;

    