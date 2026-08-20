-- Last updated: 8/20/2026, 1:57:45 AM
-- Step 1: Create a grouping key for each streak of identical results.
WITH StreakIdentifier AS (
    SELECT
        player_id,
        result,
        -- This difference is constant for any consecutive streak
        (ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY match_day)) -
        (ROW_NUMBER() OVER(PARTITION BY player_id, result ORDER BY match_day)) AS streak_group
    FROM
        Matches
),

-- Step 2: Find the length of every winning streak
WinningStreaks AS (
    SELECT
        player_id,
        COUNT(*) AS streak_length
    FROM
        StreakIdentifier
    WHERE
        result = 'Win'
    GROUP BY
        player_id, streak_group
)

-- Step 3: Select all players and LEFT JOIN to find their personal best streak
SELECT
    p.player_id,
    COALESCE(MAX(ws.streak_length), 0) AS longest_streak
FROM
    -- Start with a distinct list of all players to include everyone
    (SELECT DISTINCT player_id FROM Matches) p
LEFT JOIN
    WinningStreaks ws ON p.player_id = ws.player_id
GROUP BY
    p.player_id;