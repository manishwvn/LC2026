-- Last updated: 8/20/2026, 1:54:08 AM
SELECT tweet_id
FROM Tweets
WHERE (LENGTH(content) > 140)
    OR (content LIKE '%#%#%#%#%')
    OR (content LIKE '%@%@%@%@%')
ORDER BY tweet_id