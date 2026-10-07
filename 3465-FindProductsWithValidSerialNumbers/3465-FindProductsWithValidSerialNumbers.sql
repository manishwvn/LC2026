-- Last updated: 10/7/2026, 2:43:39 PM
SELECT 
    * 
FROM 
products WHERE description REGEXP "SN[0-9]{4}-[0-9]{4}$" 
OR description REGEXP "SN[0-9]{4}-[0-9]{4}[^0-9]+"
ORDER BY product_id