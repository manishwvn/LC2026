-- Last updated: 8/20/2026, 1:54:54 AM
select
    city
from
    listings
group by
    city
having avg(price) > (select avg(price) from listings)
order by city;