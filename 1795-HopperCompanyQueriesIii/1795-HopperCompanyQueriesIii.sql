-- Last updated: 8/20/2026, 2:00:47 AM
WITH RECURSIVE MonthWindows AS (
    SELECT 1 AS start_month, 3 AS end_month
    UNION ALL
    SELECT start_month + 1, end_month + 1
    FROM MonthWindows
    WHERE end_month < 12
),
RideData AS (
    SELECT
        month(r.requested_at) AS ride_month,
        ar.ride_distance,
        ar.ride_duration
    FROM
        Rides r
    JOIN
        AcceptedRides ar ON r.ride_id = ar.ride_id
    WHERE YEAR(r.requested_at) = 2020
),
-- CTE with corrections applied
WindowedRideData AS (
    SELECT
        mw.start_month,
        -- Correction: Use standard SUM() with COALESCE for aggregation.
        COALESCE(SUM(rd.ride_distance), 0) as sum_ride_distance,
        COALESCE(SUM(rd.ride_duration), 0) as sum_ride_duration
    FROM
        MonthWindows mw -- Correction: Start from MonthWindows to include all months.
    LEFT JOIN
        RideData rd ON rd.ride_month BETWEEN mw.start_month AND mw.end_month -- Correction: Join ride data onto the months.
    GROUP BY
        mw.start_month -- Correction: Add GROUP BY for aggregation.
)
-- Final SELECT is now simpler
SELECT
    start_month AS month,
    ROUND(sum_ride_distance / 3.0, 2) AS average_ride_distance,
    ROUND(sum_ride_duration / 3.0, 2) AS average_ride_duration
FROM WindowedRideData
ORDER BY month;