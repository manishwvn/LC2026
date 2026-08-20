-- Last updated: 8/20/2026, 1:54:52 AM
with total_scores as (select
    student_id,
    student_name,
    (assignment1+assignment2+assignment3) as total
from
    scores)

select
    max(total) - min(total) as difference_in_score
from
    total_scores;