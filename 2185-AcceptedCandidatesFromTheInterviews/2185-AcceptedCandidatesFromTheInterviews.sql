-- Last updated: 8/20/2026, 1:58:31 AM
select
    c.candidate_id
from
    candidates c
 join
    rounds r
on
    c.interview_id = r.interview_id
where
    c.years_of_exp >= 2
group by
    c.candidate_id
having
    sum(r.score) > 15;