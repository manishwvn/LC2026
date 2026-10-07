-- Last updated: 10/7/2026, 3:00:42 PM
select
    extra as report_reason,
    count(distinct post_id) as report_count
from
    actions
where
    action_date = '2019-07-04'
    and 
    action = 'report'
group by
    1;