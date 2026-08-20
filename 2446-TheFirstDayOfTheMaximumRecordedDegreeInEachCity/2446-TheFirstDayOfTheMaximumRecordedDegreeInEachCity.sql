-- Last updated: 8/20/2026, 1:56:54 AM
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