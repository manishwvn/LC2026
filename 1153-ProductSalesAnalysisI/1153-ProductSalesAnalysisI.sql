-- Last updated: 8/20/2026, 2:06:02 AM
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