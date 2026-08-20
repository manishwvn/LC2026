-- Last updated: 8/20/2026, 2:06:10 AM
select
    customer_id
from
    customer
group by
    customer_id
having
    count(distinct product_key) = (select count(distinct product_key) from product);
