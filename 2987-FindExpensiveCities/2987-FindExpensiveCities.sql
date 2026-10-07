-- Last updated: 10/7/2026, 2:46:21 PM
select
    city
from
    listings
group by
    city
having avg(price) > (select avg(price) from listings)
order by city;