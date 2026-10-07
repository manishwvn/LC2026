-- Last updated: 10/7/2026, 2:50:46 PM
with cte1 as(
    select
        first_col,
        row_number() over(order by first_col) as rnk
    from
        data),
cte2 as(
    select
        second_col,
        row_number() over(order by second_col desc) as rnk
    from
        data
)

select
    cte1.first_col,
    cte2.second_col
from
    cte1
join
    cte2
on
    cte1.rnk = cte2.rnk;