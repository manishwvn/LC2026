-- Last updated: 8/20/2026, 2:05:57 AM
SELECT product_id, year AS first_year, quantity, price
FROM (SELECT *,
            DENSE_RANK() OVER (PARTITION BY product_id ORDER BY year) AS rnk
FROM Sales) a
WHERE rnk = 1;