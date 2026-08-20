-- Last updated: 8/20/2026, 1:56:04 AM
SELECT e.symbol as metal, e1.symbol as nonmetal
FROM Elements as e
JOIN Elements as e1
ON (e.type = "Metal" AND e1.type = "Nonmetal");