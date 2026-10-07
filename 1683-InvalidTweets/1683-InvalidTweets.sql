-- Last updated: 10/7/2026, 2:54:33 PM
select
    tweet_id
from
    tweets
where char_length(content) > 15;