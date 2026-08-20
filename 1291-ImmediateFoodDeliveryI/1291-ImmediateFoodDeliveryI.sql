-- Last updated: 8/20/2026, 2:04:38 AM
SELECT 
    ROUND(
        
            COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN delivery_id ELSE NULL END) / 
        COUNT(delivery_id) * 100, 2
    ) AS immediate_percentage
FROM 
    Delivery;