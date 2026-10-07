-- Last updated: 10/7/2026, 2:44:42 PM
select
    p.product_id,
    case
        when d.discount is not null then
            p.price * ((100 - d.discount)/100)
        else
            p.price
        end as final_price,
    p.category
from
    products p
left join
    discounts d
on
    p.category = d.category
order by
    p.product_id;
