-- Last updated: 8/20/2026, 2:03:48 AM
with recursive cte as (

    -- anchor member
    select
        employee_id
    from
        employees
    where
        manager_id = 1 and employee_id <> 1

    
    union all

    select
        e.employee_id
    from 
        employees e 
    join
        cte c 
    on
        e.manager_id = c.employee_id
)

select
    *
from
    cte;