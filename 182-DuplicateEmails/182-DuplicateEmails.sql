-- Last updated: 8/20/2026, 2:16:21 AM
select
    email
from
    person
group by
    email
having count(*) > 1