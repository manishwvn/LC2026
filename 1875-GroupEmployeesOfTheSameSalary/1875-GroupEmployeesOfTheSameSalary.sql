-- Last updated: 10/7/2026, 2:53:10 PM
with cte as (select
    *,
    count(employee_id) over(partition by salary order by salary) as same_salary_emps
from
    employees),

cte2 as (
select
    *,
    dense_rank() over(order by salary) as team_id
from
    cte
where
    same_salary_emps >= 2)

select
    employee_id,
    name,
    salary,
    team_id
from
    cte2
order by
    team_id, employee_id;