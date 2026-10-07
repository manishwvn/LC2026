-- Last updated: 10/7/2026, 2:48:11 PM
SELECT e.symbol as metal, e1.symbol as nonmetal
FROM Elements as e
JOIN Elements as e1
ON (e.type = "Metal" AND e1.type = "Nonmetal");