-- Last updated: 10/7/2026, 2:53:23 PM
SELECT
    transaction_id
FROM
    (
        SELECT
            transaction_id,
            amount,
            -- For each row, find the maximum amount within its day's partition
            MAX(amount) OVER (PARTITION BY DATE(day)) as max_amount_for_day
        FROM
            Transactions
    ) AS t
WHERE
    -- Keep only the rows where the transaction's amount IS the max for that day
    t.amount = t.max_amount_for_day
ORDER BY
    transaction_id;