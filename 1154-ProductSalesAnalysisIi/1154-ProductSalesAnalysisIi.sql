-- Last updated: 8/20/2026, 2:05:58 AM
SELECT 
    PRODUCT_ID AS 'product_id',
    SUM(QUANTITY) AS 'total_quantity'
FROM
    SALES
GROUP BY
    PRODUCT_ID;
    