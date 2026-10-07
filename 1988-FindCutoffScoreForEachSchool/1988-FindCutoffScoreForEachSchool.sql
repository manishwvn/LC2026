-- Last updated: 10/7/2026, 2:52:05 PM
select
    s.school_id,
    coalesce(min(e.score), -1) as score
from
    schools s
left join
    exam e
on
    s.capacity >= e.student_count
group by
    s.school_id

