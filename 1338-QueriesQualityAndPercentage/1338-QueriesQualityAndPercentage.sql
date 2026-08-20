-- Last updated: 8/20/2026, 2:04:13 AM
select
    query_name,
    round(avg(rating/position), 2) as quality,
    round(
        avg(
        case
            when rating < 3 then 1
            else 0
            end
        )
         * 100
        ,2) as poor_query_percentage
from
    queries
where
    query_name is not null
group by
    query_name;

