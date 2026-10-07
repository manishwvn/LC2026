-- Last updated: 10/7/2026, 2:49:29 PM
select
    s.user_id,
    sum(p.price * s.quantity) as spending
from
    sales s
join
    product p
on
    s.product_id = p.product_id
group by
    s.user_id
order by
    2 desc, 1 asc;