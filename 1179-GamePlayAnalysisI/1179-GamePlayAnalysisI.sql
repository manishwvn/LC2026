-- Last updated: 8/20/2026, 2:05:41 AM
select
    player_id,
    event_date as first_login
from
    (
select
    *,
    dense_rank() over(partition by player_id order by event_date asc) as rnk
from
    activity) as t
where
    t.rnk = 1;