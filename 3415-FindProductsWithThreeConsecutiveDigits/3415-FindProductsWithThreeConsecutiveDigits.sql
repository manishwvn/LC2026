-- Last updated: 10/7/2026, 2:43:51 PM
SELECT 
    product_id, 
    name
FROM 
    Products
WHERE 
    name REGEXP '[0-9]{3}' AND name NOT REGEXP '[0-9]{4,}'
ORDER BY 
    product_id ASC;