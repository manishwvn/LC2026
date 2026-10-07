-- Last updated: 10/7/2026, 2:49:26 PM
select
    t1.team_name as home_team,
    t2.team_name as away_team
from
    teams t1
join
    teams t2
on
    t1.team_name <> t2.team_name;