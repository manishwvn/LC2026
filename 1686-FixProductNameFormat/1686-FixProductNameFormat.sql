-- Last updated: 8/20/2026, 2:01:39 AM
select
    lower(trim(product_name)) as product_name,
    date_format(sale_date, "%Y-%m") as sale_date,
    count(*) as total
from
    Sales
group by
    1, 2
order by
    1, 2;