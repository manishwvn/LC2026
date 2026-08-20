-- Last updated: 8/20/2026, 1:53:09 AM
select
    *
from
    users
where
    regexp_like(email, '[a-zA-Z0-9_]+@[a-zA-Z]+\.com$')
order by
    user_id;