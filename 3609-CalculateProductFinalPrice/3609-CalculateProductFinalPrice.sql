-- Last updated: 8/20/2026, 1:53:45 AM
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
