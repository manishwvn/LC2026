-- Last updated: 8/20/2026, 1:58:51 AM
select
    employee_id
from
    employees
where
    salary < 30000
and
    manager_id not in (
        select employee_id from employees
    )
order by
    employee_id;