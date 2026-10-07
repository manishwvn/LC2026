-- Last updated: 10/7/2026, 2:52:12 PM
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