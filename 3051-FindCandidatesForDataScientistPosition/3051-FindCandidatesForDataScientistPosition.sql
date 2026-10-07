-- Last updated: 10/7/2026, 2:46:30 PM
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