-- Last updated: 10/7/2026, 2:43:44 PM
select
    *
from
    users
where
    regexp_like(email, '[a-zA-Z0-9_]+@[a-zA-Z]+\.com$')
order by
    user_id;