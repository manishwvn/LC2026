-- Last updated: 10/7/2026, 3:01:43 PM
select
    customer_id
from
    customer
group by
    customer_id
having
    count(distinct product_key) = (select count(distinct product_key) from product);
