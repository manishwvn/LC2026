-- Last updated: 10/7/2026, 2:51:32 PM
SELECT 
    account_id, 
    day, 
    sum(case when type = 'Deposit' then amount else -amount end) 
    over(partition by account_id order by day asc)     
    as balance 
FROM 
    transactions
