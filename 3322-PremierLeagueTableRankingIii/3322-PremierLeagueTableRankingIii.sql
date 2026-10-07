-- Last updated: 10/7/2026, 2:44:20 PM
select
    season_id,
    team_id,
    team_name,
    (3*wins + 1*draws) as points,
    (goals_for - goals_against) as goal_difference,
    row_number() over(partition by season_id order by (3*wins + 1*draws) desc,
        (goals_for - goals_against) desc, team_name asc)
        as position
from
    seasonstats
group by
    season_id,
    team_id,
    team_name
order by
    season_id,
    position,
    team_name;
