-- Last updated: 10/7/2026, 3:01:31 PM
select
    p.product_name,
    s.year,
    s.price
from
    sales s
 join
    product p
on
    p.product_id = s.product_id;