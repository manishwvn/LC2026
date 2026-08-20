-- Last updated: 8/20/2026, 2:10:47 AM
select
    id,
    case
        when p_id is null then 'Root'
        when id not in (select distinct p_id from tree where p_id is not null)
            then 'Leaf'
        else 'Inner'
    end as type
from
    tree
order by
    id;