-- Last updated: 10/7/2026, 2:45:09 PM
select
    state,
    group_concat(city order by city separator ', ') as cities
from
    cities
group by
    state
order by
    state;
