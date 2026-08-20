-- Last updated: 8/20/2026, 1:58:20 AM
SELECT 
    account_id, 
    day, 
    sum(case when type = 'Deposit' then amount else -amount end) 
    over(partition by account_id order by day asc)     
    as balance 
FROM 
    transactions
