-- Last updated: 10/7/2026, 2:48:07 PM
select
    person_id,
    concat(name , '(' , substring(profession, 1, 1) , ')') as name
from
    person
order by person_id desc;