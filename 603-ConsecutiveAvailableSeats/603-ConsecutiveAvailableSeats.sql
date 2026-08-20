-- Last updated: 8/20/2026, 2:10:56 AM
select
    seat_id
from (
    select
    *,
    lag(free, 1, 0) over(order by seat_id) as prev,
    lead(free, 1, 0) over(order by seat_id) as next
from
    cinema
) t
where
    t.free = 1 and (t.prev = 1 or t.next = 1)
order by
    seat_id

