-- Last updated: 10/7/2026, 3:00:10 PM
SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY 1;