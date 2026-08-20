-- Last updated: 8/20/2026, 2:00:37 AM
select
    tweet_id
from
    tweets
where char_length(content) > 15;