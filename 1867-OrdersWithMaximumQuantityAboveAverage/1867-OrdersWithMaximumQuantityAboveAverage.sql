-- Last updated: 10/7/2026, 2:53:13 PM
with cte as(select
    order_id,
    max(quantity) as max_order,
    avg(quantity) as avg_order

from
    ordersdetails
group by
    order_id)

select
    order_id
from
    cte
where
    max_order > (select max(avg_order) from cte)