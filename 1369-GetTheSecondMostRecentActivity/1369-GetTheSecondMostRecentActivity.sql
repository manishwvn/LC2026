-- Last updated: 10/7/2026, 2:57:27 PM
with cte as (select
    distinct *
from
    useractivity),

cte2 as (
select
    *,
    dense_rank() over(partition by username order by startDate desc) rnk,
    count(activity) over(partition by username) as num_activities
from
    cte)

select
    username,
    activity,
    startDate,
    endDate
from
    cte2
where
    rnk = 2
    or
    num_activities = 1;