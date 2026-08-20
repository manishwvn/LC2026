-- Last updated: 8/20/2026, 2:04:58 AM
SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY 1;