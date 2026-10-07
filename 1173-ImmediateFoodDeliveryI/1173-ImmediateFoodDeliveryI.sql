-- Last updated: 10/7/2026, 2:59:43 PM
SELECT 
    ROUND(
        
            COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN delivery_id ELSE NULL END) / 
        COUNT(delivery_id) * 100, 2
    ) AS immediate_percentage
FROM 
    Delivery;