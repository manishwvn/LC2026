-- Last updated: 8/20/2026, 1:55:45 AM
select
    bike_number,
    max(end_time) as end_time
from
    bikes
group by
    bike_number
order by
    end_time desc;