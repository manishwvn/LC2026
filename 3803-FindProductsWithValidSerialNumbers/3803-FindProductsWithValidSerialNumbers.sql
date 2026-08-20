-- Last updated: 8/20/2026, 1:53:04 AM
SELECT 
    * 
FROM 
products WHERE description REGEXP "SN[0-9]{4}-[0-9]{4}$" 
OR description REGEXP "SN[0-9]{4}-[0-9]{4}[^0-9]+"
ORDER BY product_id