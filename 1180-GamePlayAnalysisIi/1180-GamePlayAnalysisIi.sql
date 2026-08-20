-- Last updated: 8/20/2026, 2:05:41 AM
select
    a.player_id, a.device_id
from
    activity a
join
    (select
        player_id,
        min(event_date) as first
    from
        activity
    group by 1) b
    on
        a.player_id = b.player_id
        and
        a.event_date = b.first