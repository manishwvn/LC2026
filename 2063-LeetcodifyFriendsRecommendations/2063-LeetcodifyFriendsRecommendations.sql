-- Last updated: 8/20/2026, 1:59:14 AM
WITH cte AS (
    SELECT 
        l1.user_id AS user1_id, 
        l2.user_id AS user2_id
    FROM listens l1
    JOIN listens l2 
        ON l1.day = l2.day 
        AND l1.song_id = l2.song_id 
        AND l1.user_id <> l2.user_id
    GROUP BY l1.user_id, l2.user_id, l1.day
    HAVING COUNT(DISTINCT l2.song_id) >= 3
)

SELECT distinct c.user1_id AS user_id, c.user2_id AS recommended_id
FROM cte c
LEFT JOIN friendship f 
    ON (c.user1_id = f.user1_id AND c.user2_id = f.user2_id) 
    OR (c.user1_id = f.user2_id AND c.user2_id = f.user1_id)
WHERE f.user1_id IS NULL;