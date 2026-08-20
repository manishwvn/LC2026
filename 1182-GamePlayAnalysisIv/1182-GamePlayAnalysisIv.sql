-- Last updated: 8/20/2026, 2:05:40 AM
WITH login_ranks AS (
    SELECT
        player_id,
        event_date,
        DENSE_RANK() OVER(PARTITION BY player_id ORDER BY event_date) as login_rank
    FROM
        Activity
)
SELECT
    ROUND(
        COUNT(t2.player_id) / COUNT(t1.player_id),
        2
    ) AS fraction
FROM
    login_ranks t1
LEFT JOIN
    login_ranks t2 ON t1.player_id = t2.player_id AND t2.login_rank = 2 AND t2.event_date = t1.event_date + INTERVAL '1' DAY
WHERE
    t1.login_rank = 1;