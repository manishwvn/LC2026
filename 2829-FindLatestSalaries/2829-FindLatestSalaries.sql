-- Last updated: 8/20/2026, 1:55:48 AM
select
    emp_id,
    firstname,
    lastname,
    max(salary) as salary,
    department_id
from
    Salary
group by
    emp_id,
    firstname,
    lastname,
    department_id
order by
    emp_id;