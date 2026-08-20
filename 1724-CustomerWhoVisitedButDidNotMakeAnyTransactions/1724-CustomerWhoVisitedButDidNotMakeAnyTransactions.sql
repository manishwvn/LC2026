-- Last updated: 8/20/2026, 2:01:24 AM
-- select
--     v.customer_id as customer_id,
--     count(v.visit_id) as count_no_trans
-- from
--     visits v
-- left join
--     transactions t
-- on
--     v.visit_id = t.visit_id
-- where
--     t.visit_id is null
-- group by
--     v.customer_id;

select
    v.customer_id, count(*) as count_no_trans
from
    visits v 
left join
    transactions t
on
    v.visit_id = t.visit_id
where
    t.visit_id is null
group by
    v.customer_id;
