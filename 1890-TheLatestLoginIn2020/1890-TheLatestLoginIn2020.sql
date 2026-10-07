-- Last updated: 10/7/2026, 2:52:58 PM
SELECT 
    USER_ID AS 'user_id',
    MAX(TIME_STAMP) AS 'last_stamp'
FROM 
    LOGINS
WHERE
    YEAR(TIME_STAMP) = '2020'
GROUP BY
    USER_ID;

    