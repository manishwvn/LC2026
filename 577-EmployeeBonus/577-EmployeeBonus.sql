-- Last updated: 8/20/2026, 2:11:17 AM
select
    e.name as name,
    b.bonus as bonus
from
    employee e
left join
    bonus b
on
    e.empid = b.empid
where
    coalesce(b.bonus, 0) < 1000;