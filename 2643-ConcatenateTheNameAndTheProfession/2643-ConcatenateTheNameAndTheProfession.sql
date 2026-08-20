-- Last updated: 8/20/2026, 1:56:01 AM
select
    person_id,
    concat(name , '(' , substring(profession, 1, 1) , ')') as name
from
    person
order by person_id desc;