-- Last updated: 8/20/2026, 2:02:31 AM
with cte as (select
        *,
        min(score) over(partition by exam_id) as min_score,
        max(score) over(partition by exam_id) as max_score
    from
        exam),

cte2 as(
    select
        distinct student_id
    from
        cte
    where
        score = min_score or score = max_score
)

select
    *
from
    student 
where
    student_id in (select distinct student_id from exam)
    and
    student_id not in (select distinct student_id from cte2)
order by 1;