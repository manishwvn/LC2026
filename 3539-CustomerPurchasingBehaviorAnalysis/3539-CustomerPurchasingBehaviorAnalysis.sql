-- Last updated: 8/20/2026, 1:53:59 AM
with cte as (
    select 
        t.customer_id,
        p.category, 
        rank() 
            over(partition by t.customer_id 
                order by count(*) desc, max(t.transaction_date) desc) as rnk
    from 
        Transactions t 
    left join
        products p 
    on
        t.product_id = p.product_id
   group by t.customer_id,p.category
)



select
    t.customer_id as customer_id,
    sum(t.amount) as total_amount,
    count(t.transaction_id) as transaction_count,
    count(distinct p.category) as unique_categories,
    round(avg(amount), 2) as avg_transaction_amount,
    m.category as top_category,
    round((count(t.transaction_id) * 10) + (sum(amount) / 100), 2) as loyalty_score
from
    transactions t
left join
    products p
on
    t.product_id = p.product_id
left join
    (select customer_id, category from cte where rnk = 1) as m
on
    t.customer_id = m.customer_id 
group by
    t.customer_id
order by
    loyalty_score desc, customer_id;