-- Last updated: 8/20/2026, 2:10:46 AM
select
    x,
    y,
    z,
    case 
        when (x+y) > z and (x + z) > y and (y + z) > x then 'Yes'
        else 'No'
    end as triangle
from
    Triangle;