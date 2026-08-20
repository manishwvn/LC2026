-- Last updated: 8/20/2026, 1:52:53 AM
SELECT user_id,
       ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration,
       ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity
-- WHERE activity_type IN ('free_trial', 'paid')
GROUP BY user_id
-- HAVING COUNT(DISTINCT activity_type) = 2;
HAVING
    trial_avg_duration is not null
    and
    paid_avg_duration is not null
ORDER BY
    user_id;