-- Last updated: 10/7/2026, 2:59:16 PM
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