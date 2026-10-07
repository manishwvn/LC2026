-- Last updated: 10/7/2026, 3:01:28 PM
SELECT 
    PRODUCT_ID AS 'product_id',
    SUM(QUANTITY) AS 'total_quantity'
FROM
    SALES
GROUP BY
    PRODUCT_ID;
    