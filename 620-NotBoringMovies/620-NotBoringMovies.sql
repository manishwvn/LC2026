-- Last updated: 8/20/2026, 2:10:35 AM
SELECT
    *
FROM
    CINEMA
WHERE
    ID % 2 <> 0
AND lower(description) not like '%boring%'
ORDER BY RATING DESC;