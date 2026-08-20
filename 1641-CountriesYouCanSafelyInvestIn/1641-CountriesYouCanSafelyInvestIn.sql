-- Last updated: 8/20/2026, 2:01:58 AM
WITH CallDetails AS (
    SELECT
        C.NAME AS country,
        S.DURATION,
        -- Use a window function to get the overall average
        -- and attach it to every single row.
        AVG(S.DURATION) OVER () AS GlobalAvgDuration
    FROM
        COUNTRY C
    JOIN
        PERSON P ON SUBSTR(P.PHONE_NUMBER, 1, 3) = C.COUNTRY_CODE
    JOIN
        CALLS S ON P.ID = S.CALLER_ID OR P.ID = S.CALLEE_ID
)
-- Now, aggregate the prepared data from the CTE
SELECT
    country
FROM
    CallDetails
GROUP BY
    country, GlobalAvgDuration -- Must group by the non-aggregated columns
HAVING
    -- Compare the country's average to the global average
    AVG(DURATION) > GlobalAvgDuration;