-- Last updated: 10/7/2026, 2:49:37 PM
select
    count(case when dayofweek(submit_date) in (1, 7) then task_id end) as weekend_cnt,
    count(case when dayofweek(submit_date) not in (1,7) then task_id end) as working_cnt
from
    tasks;