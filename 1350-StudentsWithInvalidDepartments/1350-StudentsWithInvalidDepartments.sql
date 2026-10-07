-- Last updated: 10/7/2026, 2:57:47 PM
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