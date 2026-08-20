-- Last updated: 8/20/2026, 2:04:15 AM
with cte as (select
    *,
    sum(weight) over(order by turn) as cum_sum
from
    queue)

select
    person_name
from
    cte
where 
    cum_sum <= 1000
order by cum_sum desc
limit 1;