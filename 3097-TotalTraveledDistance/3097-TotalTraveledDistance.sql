-- Last updated: 8/20/2026, 1:55:24 AM
select
    u.user_id,
    u.name,
    ifnull(sum(r.distance), 0) as 'traveled distance'
from
    users u
left join
    rides r
on
    u.user_id = r.user_id
group by
    u.user_id
order by
    u.user_id;