-- Last updated: 10/7/2026, 2:54:03 PM
select
    event_day as day,
    emp_id,
    sum(out_time - in_time) as total_time
from
    employees
group by
    event_day, emp_id;