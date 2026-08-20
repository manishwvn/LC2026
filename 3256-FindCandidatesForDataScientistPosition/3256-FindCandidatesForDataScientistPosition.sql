-- Last updated: 8/20/2026, 1:55:00 AM
select
    candidate_id
from
    candidates
where
    skill in ('Python', 'Tableau','PostgreSQL')
group by
    candidate_id
having
    count(skill) = 3
order by
    1;