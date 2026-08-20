-- Last updated: 8/20/2026, 2:00:25 AM
select
     user_id,
    count(follower_id) as followers_count
from
    followers
group by
    user_id
order by 1;