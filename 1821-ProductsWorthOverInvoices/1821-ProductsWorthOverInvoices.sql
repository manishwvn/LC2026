-- Last updated: 8/20/2026, 2:00:36 AM
SELECT 
    P.NAME AS 'name', 
    IFNULL(SUM(I.REST), 0) AS 'rest',
    IFNULL(SUM(I.PAID), 0) AS 'paid',
    IFNULL(SUM(I.CANCELED), 0) AS 'canceled',
    IFNULL(SUM(I.REFUNDED), 0) AS 'refunded'
FROM
    PRODUCT P
LEFT JOIN
    INVOICE I
ON
    P.PRODUCT_ID  = I.PRODUCT_ID
GROUP BY
    P.PRODUCT_ID
ORDER BY
    P.NAME;
    
