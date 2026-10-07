-- Last updated: 10/7/2026, 2:45:14 PM
select
    u.user_id
from
    emails u
join
    texts t
on
    u.email_id = t.email_id
where
    t.signup_action = 'Verified'
and
    date(t.action_date) = date_add(date(u.signup_date), interval 1 day)
order by
    1;