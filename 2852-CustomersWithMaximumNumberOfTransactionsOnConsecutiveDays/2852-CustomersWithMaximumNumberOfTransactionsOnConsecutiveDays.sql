-- Last updated: 8/20/2026, 1:55:42 AM
with cte as (select
    *,
    row_number() over(partition by customer_id order by transaction_date) as date_rnk
from
    transactions),

cte2 as (
select
    customer_id,
    count(transaction_id) as purchases
from
    cte
group by
    customer_id, date_sub(transaction_date, interval date_rnk day)),

cte3 as (select
    *,
    dense_rank() over(order by purchases desc) rnk
from
    cte2)

select
    customer_id
from
    cte3
where
    rnk = 1
order by
    1;