-- Last updated: 8/20/2026, 2:16:18 AM
select
    c.name as Customers
from
    Customers c
left join
    orders o
on
    c.id = o.customerid
where
    o.id is null;