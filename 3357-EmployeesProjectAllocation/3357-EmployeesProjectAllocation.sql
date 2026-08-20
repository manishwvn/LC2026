-- Last updated: 8/20/2026, 1:54:34 AM
with cte as (select
    p.*,
    e.name,
    e.team,
    avg(p.workload) over(partition by e.team) as avg_workload
from
    project p
join
    employees e
on
    p.employee_id = e.employee_id)

select
    EMPLOYEE_ID,
    PROJECT_ID,
    name as EMPLOYEE_NAME,
    workload as PROJECT_WORKLOAD
from
    cte
where
    workload > avg_workload
order by
    1, 2;