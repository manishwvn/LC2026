-- Last updated: 8/20/2026, 2:16:31 AM
select
    p.firstName,
    p.lastName,
    a.city,
    a.state
from
    person p
left join
    address a
on
    p.personId = a.personId;