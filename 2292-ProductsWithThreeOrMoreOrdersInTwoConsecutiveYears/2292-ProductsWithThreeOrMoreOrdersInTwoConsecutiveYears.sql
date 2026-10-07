-- Last updated: 10/7/2026, 2:49:45 PM
with cte as(
    select
        product_id,
        year(purchase_date),
        count(*),
        year(purchase_date) - row_number() over(partition by product_id order by year(purchase_date)) as diff
    from
        orders
    group by product_id, year(purchase_date)
    having count(*) >= 3)

select
    distinct
    product_id
from
    cte
group by
    product_id, diff
having
    count(*) >= 2