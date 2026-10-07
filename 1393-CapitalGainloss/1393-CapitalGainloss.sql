-- Last updated: 10/7/2026, 2:57:16 PM
SELECT 
    stock_name,
    SUM(
        CASE 
            WHEN operation = 'buy' THEN -price
            WHEN operation = 'sell' THEN price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name