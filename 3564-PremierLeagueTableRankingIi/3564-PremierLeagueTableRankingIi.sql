-- Last updated: 8/20/2026, 1:53:55 AM
with cte as (
    select
        team_name,
        (wins * 3 + draws * 1) as points
    from
        teamstats
),

cte2 as (
select
    *,
    rank() over(order by points desc) as position
from
    cte),

cte3 as (
select
    count(team_id) as counts
from
    teamstats)

select
    *,
    case
        when position < (0.33 * (select * from cte3)+1) then 'Tier 1'
        when position > (0.33 * (select * from cte3)+1)
            and
            position < (0.66 * (select * from cte3)+1) then 'Tier 2'
        else 'Tier 3' 
    end as tier
from
    cte2
order by
    points desc, team_name asc;