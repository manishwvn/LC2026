-- Last updated: 10/7/2026, 2:50:39 PM
with cte as (select
    t.team_id,
    t.name,
    t.points,
    p.points_change,
    dense_rank() over(order by t.points desc, t.name) as initial_rank,
    dense_rank() over(order by t.points+p.points_change desc, t.name) as final_rank 
from
    teampoints t
join
    pointschange p
on
    t.team_id = p.team_id)

select
    team_id,
    name,
    cast(initial_rank as signed) - cast(final_rank as signed) as rank_diff
from
    cte;