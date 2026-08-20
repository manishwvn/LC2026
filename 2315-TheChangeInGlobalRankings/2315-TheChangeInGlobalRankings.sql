-- Last updated: 8/20/2026, 1:57:44 AM
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