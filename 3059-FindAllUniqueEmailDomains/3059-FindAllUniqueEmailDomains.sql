-- Last updated: 10/7/2026, 2:45:52 PM
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