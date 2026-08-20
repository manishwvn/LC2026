-- Last updated: 8/20/2026, 2:04:02 AM
SELECT
    S1.sub_id AS post_id,
    COUNT(DISTINCT S2.sub_id) AS number_of_comments
FROM
    Submissions S1
LEFT JOIN
    Submissions S2
ON
    S1.sub_id = S2.parent_id
WHERE S1.parent_id IS NULL
GROUP BY S1.sub_id