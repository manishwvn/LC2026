-- Last updated: 10/7/2026, 2:47:01 PM
with cte as (select
    ceil(minute / 6) as interval_no,
    order_count
from
    orders)

select
    interval_no,
    sum(order_count) as total_orders
from
    cte
group by
    1
order by
    1;