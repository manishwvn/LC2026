-- Last updated: 8/20/2026, 1:54:59 AM
WITH cte AS (
    SELECT
        item_type,
        SUM(square_footage) AS area,
        COUNT(item_id) AS num,
        CASE 
            WHEN SUM(square_footage) = 0 THEN 0 -- Or some other appropriate default for max_comb
            ELSE FLOOR(500000 / SUM(square_footage)) 
        END AS max_comb
    FROM
        inventory
    GROUP BY
        item_type
),
prime_data AS (
  SELECT CASE WHEN area * max_comb IS NULL THEN 0 ELSE area * max_comb END as prime_total_area FROM cte WHERE item_type = 'prime_eligible' -- Handle possible NULL
),
remaining_space AS (
  SELECT 500000 - prime_total_area as space FROM prime_data
)
SELECT
    item_type,
    CASE
        WHEN item_type = 'prime_eligible' THEN num * max_comb
        ELSE CASE
                 WHEN area = 0 THEN 0  -- Handle division by zero
                 ELSE FLOOR( (SELECT space FROM remaining_space) / area) * num
             END
    END AS item_count
FROM
    cte
ORDER BY 2 DESC;