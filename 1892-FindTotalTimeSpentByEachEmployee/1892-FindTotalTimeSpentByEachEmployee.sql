-- Last updated: 8/20/2026, 2:00:12 AM
select
    event_day as day,
    emp_id,
    sum(out_time - in_time) as total_time
from
    employees
group by
    event_day, emp_id;