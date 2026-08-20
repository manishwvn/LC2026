-- Last updated: 8/20/2026, 2:11:01 AM
select
    class
from
    courses
group by class
having count(distinct student) >= 5;