-- Last updated: 8/20/2026, 1:54:04 AM
select
    state,
    group_concat(city order by city separator ', ') as cities
from
    cities
group by
    state
order by
    state;
