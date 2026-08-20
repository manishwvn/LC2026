-- Last updated: 8/20/2026, 2:01:33 AM
with cte as (select
    u.user_id,
    u.user_name,
    coalesce(sum(case
        when u.user_id = t.paid_by then -1 * amount
        else amount
    end), 0) + u.credit as credit
from
    users u
left join
    transactions t
on
    u.user_id = t.paid_by
    or
    u.user_id = t.paid_to
group by
    u.user_id)

select
    user_id,
    user_name,
    credit,
    case when credit > 0 then 'No' else 'Yes' end
        as 'credit_limit_breached'
from
    cte;