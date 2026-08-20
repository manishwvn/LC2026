-- Last updated: 8/20/2026, 1:54:37 AM
with cte as (select
    age_bucket,
    sum(case when activity_type = 'send' then time_spent else 0 end) as send_time,
    sum(case when activity_type = 'open' then time_spent else 0 end) as open_time
from
    activities a1
join
    age a2
on
    a1.user_id = a2.user_id
group by
    age_bucket)

select
    age_bucket,
    round((send_time / (send_time + open_time))*100,2) as send_perc,
    round((open_time / (send_time +open_time))*100,2) as open_perc
from
    cte;