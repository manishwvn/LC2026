-- Last updated: 8/20/2026, 2:05:20 AM
with cte as (
select
    *,
    avg(occurrences) over(partition by event_type) as avg
from
    events
)

select
    business_id
from
    cte
where
    occurrences > avg
group by
    business_id
having
    count(*) > 1