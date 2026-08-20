-- Last updated: 8/20/2026, 2:01:10 AM
with recursive cte as(
    select 1 as ids
    union
    select ids+1 from cte
        where ids < (select max(customer_id) from customers)
)

select
    *
from
    cte
where
    ids not in (select customer_id from customers)
order by
    ids;