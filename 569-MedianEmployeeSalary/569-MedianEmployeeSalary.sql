-- Last updated: 8/20/2026, 2:11:24 AM
with cte as (
    select
        *,
        row_number() over(partition by company order by salary) as rnk,
        count(*) over(partition by company) as counts
    from
        employee)

select
    id, company, salary
from
    cte
where
    rnk between (counts/2) and (counts/2) + 1;