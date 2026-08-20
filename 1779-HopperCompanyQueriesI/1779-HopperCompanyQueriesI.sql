-- Last updated: 8/20/2026, 2:00:59 AM
with recursive cte as(
    select
        1 as month
    union all
    select
        month + 1
    from
        cte
    where
        month < 12
),

driver as (
    select 
        driver_id,
        case
            when year(join_date) < 2020 then 1
            else month(join_date)
        end as month
    from
        drivers
    where
        year(join_date) <= 2020
),

ride as (
    select
        month(r.requested_at) as month,
        a.ride_id
    from
        acceptedrides a
    join
        rides r
    on
        r.ride_id = a.ride_id
    where
        year(r.requested_at) = 2020
)

select
    c.month,
    count(distinct d.driver_id) as active_drivers,
    coalesce(count(distinct r.ride_id), 0) as accepted_rides
from
    cte c
left join
    driver d
on
    d.month <= c.month
left join
    ride r
on
    c.month = r.month
group by
    c.month
order by
    c.month;