-- Last updated: 10/7/2026, 2:44:14 PM
select
    state,
    group_concat(city order by city SEPARATOR ', ') as cities,
    coalesce(sum(case when substring(state, 1, 1) = substring(city, 1, 1) then 1 end), 0)
        as matching_letter_count
from
    cities
group by
    state
having
    count(city) >= 3 and matching_letter_count >0
order by
    matching_letter_count desc, state asc;