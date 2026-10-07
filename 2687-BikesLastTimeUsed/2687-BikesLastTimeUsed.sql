-- Last updated: 10/7/2026, 2:47:34 PM
select
    bike_number,
    max(end_time) as end_time
from
    bikes
group by
    bike_number
order by
    end_time desc;