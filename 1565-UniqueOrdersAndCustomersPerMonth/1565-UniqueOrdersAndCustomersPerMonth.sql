-- Last updated: 10/7/2026, 2:55:41 PM
SELECT
    DATE_FORMAT(ORDER_DATE, '%Y-%m') as 'month',
    COUNT(DISTINCT ORDER_ID) AS 'order_count',
    COUNT(DISTINCT CUSTOMER_ID) AS 'customer_count'    
FROM
    ORDERS
WHERE
    INVOICE > 20
GROUP BY
    month;

    
    