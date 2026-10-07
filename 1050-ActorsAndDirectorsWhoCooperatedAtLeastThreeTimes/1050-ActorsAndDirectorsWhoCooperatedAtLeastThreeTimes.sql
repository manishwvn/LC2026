-- Last updated: 10/7/2026, 3:01:42 PM
select
    actor_id,
    director_id
from
    ActorDirector
group by
    actor_id, director_id
having count(timestamp) >= 3
