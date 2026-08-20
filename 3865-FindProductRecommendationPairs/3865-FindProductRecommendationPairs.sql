-- Last updated: 8/20/2026, 1:52:49 AM
with cte as (select
    o1.*, p1.category
from
    ProductPurchases o1
join
    ProductInfo p1
on
    o1.product_id = p1.product_id),

cte2 as (
select
    c1.user_id, 
    c1.product_id as product1_id, 
    c2.product_id as product2_id,
    c1.category as product1_category,
    c2.category as product2_category
from
    cte c1
join
    cte c2
on
    c1.user_id = c2.user_id
    and
    c1.product_id < c2.product_id)

select
    product1_id,
    product2_id,
    product1_category,
    product2_category,
    count(distinct user_id) as customer_count
from
    cte2
group by
    product1_id, product2_id, product1_category, product2_category
having
    customer_count >= 3
order by
    5 desc, 1, 2

