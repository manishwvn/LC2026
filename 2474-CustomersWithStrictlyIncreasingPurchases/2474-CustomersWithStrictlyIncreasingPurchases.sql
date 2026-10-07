-- Last updated: 10/7/2026, 2:48:22 PM
with cte as(
    select
        customer_id,
        order_date,
        sum(price) as total,
        max(year(order_date)) over(partition by customer_id) - min(year(order_date)) over(partition by customer_id)+1
            as num_years,
        dense_rank() over(partition by customer_id order by year(order_date)) as year_rnk,
        dense_rank() over(partition by customer_id order by sum(price)) as total_rnk
    from
        orders
    group by
        customer_id, year(order_date))

select
    customer_id
from
    cte
group by
    customer_id
having sum(case when year_rnk = total_rnk then 1 else 0 end) = max(num_years)
   
    