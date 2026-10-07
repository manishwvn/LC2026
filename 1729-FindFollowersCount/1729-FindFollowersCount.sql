-- Last updated: 10/7/2026, 2:54:13 PM
select
     user_id,
    count(follower_id) as followers_count
from
    followers
group by
    user_id
order by 1;