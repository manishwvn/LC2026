-- Last updated: 8/20/2026, 2:03:40 AM
with rnks as (
    select
        log_id,
        log_id - row_number() over(order by log_id) as grp
    from
        logs)

select
    min(log_id) as start_id,
    max(log_id) as end_id
from
    rnks
group by
    grp 
order by
    1;