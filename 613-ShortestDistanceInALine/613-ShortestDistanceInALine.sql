-- Last updated: 8/20/2026, 2:10:43 AM
select
    min(abs(p1.x - p2.x)) as shortest
from
    point p1
join
    point p2
on
    p1.x != p2.x;