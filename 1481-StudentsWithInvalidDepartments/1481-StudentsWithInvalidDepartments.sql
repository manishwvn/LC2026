-- Last updated: 8/20/2026, 2:03:08 AM
select
    s.id, s.name
from
    students s
left join
    departments d
on
    d.id = s.department_id
where
    d.id is null