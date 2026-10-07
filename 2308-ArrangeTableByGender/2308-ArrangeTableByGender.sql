-- Last updated: 10/7/2026, 2:49:35 PM
with cte as (select
    *,
    rank() over(partition by gender order by user_id) as rnk1,
    case
        when gender = 'female' then 1
        when gender = 'other' then 2
        else 3 
    end as rnk2
from
    genders)

select
    user_id,
    gender
from
    cte
order by rnk1, rnk2;