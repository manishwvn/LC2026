-- Last updated: 10/7/2026, 2:45:39 PM
WITH seven_day_counts AS (
    SELECT 
        user_id, 
        COUNT(post_id) OVER (
            PARTITION BY user_id 
            ORDER BY post_date 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS post_freq,
        COUNT(post_id) OVER (PARTITION BY user_id) / 4.0 AS avg_weekly_posts
    FROM posts
    WHERE post_date BETWEEN '2024-02-01' AND '2024-02-28'
)
SELECT 
    user_id, 
    MAX(post_freq) AS max_7day_posts, 
    avg_weekly_posts
FROM seven_day_counts
GROUP BY user_id, avg_weekly_posts
HAVING max_7day_posts >= 2 * avg_weekly_posts
ORDER BY user_id;