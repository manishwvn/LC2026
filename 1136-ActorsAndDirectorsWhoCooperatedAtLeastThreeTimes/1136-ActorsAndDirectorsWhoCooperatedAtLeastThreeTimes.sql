-- Last updated: 8/20/2026, 2:06:07 AM
select
    actor_id,
    director_id
from
    ActorDirector
group by
    actor_id, director_id
having count(timestamp) >= 3
