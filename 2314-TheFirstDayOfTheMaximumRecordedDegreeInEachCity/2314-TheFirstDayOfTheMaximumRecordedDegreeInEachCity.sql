-- Last updated: 10/7/2026, 2:49:32 PM
with cte as (
    select
        *,
        dense_rank() over(partition by city_id order by degree desc, day asc) as max_temp
    from
        weather)

select
    city_id,
    day,
    degree
from
    cte
where
    max_temp = 1;