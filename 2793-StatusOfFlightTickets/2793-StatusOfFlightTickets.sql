-- Last updated: 10/7/2026, 2:47:15 PM
with cte as (select
    p.*,
    f.capacity,
    row_number() over(partition by p.flight_id order by p.booking_time) as rolling_count
from
    passengers p
join
    flights f
on
    p.flight_id = f.flight_id)

select
    passenger_id,
    case when rolling_count <= capacity then 'Confirmed'
    else 'Waitlist'
    end as 'Status'
from
    cte
order by
    1;