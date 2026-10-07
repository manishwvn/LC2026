-- Last updated: 10/7/2026, 3:01:27 PM
SELECT product_id, year AS first_year, quantity, price
FROM (SELECT *,
            DENSE_RANK() OVER (PARTITION BY product_id ORDER BY year) AS rnk
FROM Sales) a
WHERE rnk = 1;