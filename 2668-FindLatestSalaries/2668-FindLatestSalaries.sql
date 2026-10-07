-- Last updated: 10/7/2026, 2:47:38 PM
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