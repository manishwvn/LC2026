-- Last updated: 8/20/2026, 2:00:09 AM
select
    distinct l1.account_id
from
    loginfo l1
join
    loginfo l2
on
    l1.account_id = l2.account_id
    and
    l1.ip_address <> l2.ip_address
where
    l1.login <= l2.logout and l2.login <= l1.logout
    
