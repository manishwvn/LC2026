-- Last updated: 8/20/2026, 2:02:21 AM
SELECT
    A.SALE_DATE as 'sale_date',
    A.SOLD_NUM - B.SOLD_NUM AS 'diff'
FROM
    SALES A
JOIN
    SALES B
ON
    A.SALE_DATE = B.SALE_DATE
and
    A.FRUIT = 'apples' and B.FRUIT = 'oranges'
ORDER BY
    A.SALE_DATE;