-- Last updated: 10/7/2026, 3:01:05 PM
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