-- Last updated: 10/7/2026, 3:00:24 PM
select
   activity_date as day,
   count(distinct user_id) as active_users
from
    activity
where
    activity_date between DATE('2019-07-27') - INTERVAL 29 DAY AND DATE('2019-07-27')
group by
    activity_date
having
    count(activity_type) >= 1;