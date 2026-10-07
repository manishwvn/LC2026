-- Last updated: 10/7/2026, 2:45:19 PM
with cte as (select
    seat_id,
    row_number() over(order by seat_id) as rnk
from
    cinema
where
    free = 1),

cte2 as (select
    seat_id,
    seat_id - rnk as grp
from
    cte),

cte3 as (
select
    grp,
    min(seat_id) as first_seat_id,
    max(seat_id) as last_seat_id,
    count(*) as consecutive_seats_len,
    dense_rank() over(order by count(*) desc) as rnk
from
    cte2
group by
    grp)

select
    first_seat_id,
    last_seat_id,
    consecutive_seats_len
from
    cte3
where
    rnk = 1
order by
    1;