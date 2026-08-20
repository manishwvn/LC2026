-- Last updated: 8/20/2026, 1:54:30 AM
select
    substring_index(email, '@', -1) as email_domain,
    count(email) as count
from
    emails
where
    email like '%.com'
group by
    email_domain
order by 1;