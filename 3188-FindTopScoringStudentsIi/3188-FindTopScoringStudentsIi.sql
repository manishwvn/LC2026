-- Last updated: 10/7/2026, 2:45:12 PM
with cte as (select
    s.*,
    c.course_id,
    c.mandatory
from
    students s
left join
    courses c
on
    s.major = c.major),

cte2 as (
select
    c.*,
    e.grade,
    e.gpa
from
    cte c
left join
    enrollments e
on
    c.course_id = e.course_id
    and c.student_id = e.student_id),

cte3 as (
select
    *
from
    cte2
group by
    student_id
having
    sum(if(mandatory = 'Yes',1, 0)) = sum(if(mandatory = 'Yes', 1, 0) * if(grade = 'A', 1, 0))
    and
    sum(if(mandatory = 'No', 1, 0) * if(grade in ('A', 'B'), 1, 0)) >= 2)

select
    student_id
from
    cte3
where
    student_id in (select student_id from enrollments group by student_id having avg(gpa)>= 2.5);