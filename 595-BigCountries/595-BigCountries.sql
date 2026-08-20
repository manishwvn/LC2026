-- Last updated: 8/20/2026, 2:11:04 AM
# SELECT 
#     NAME AS 'name',
#     POPULATION AS 'population',
#     AREA AS 'area'
# FROM 
#     WORLD
# WHERE 
#     AREA >= 3000000 OR 
#     POPULATION >= 25000000;


WITH BIG_COUNTRIES AS (
    SELECT 
        NAME AS name,
        POPULATION AS population,
        AREA as area
    FROM 
        WORLD
    WHERE 
        AREA >= 3000000 
        OR 
        POPULATION >= 25000000
)

SELECT 
    * 
FROM 
    BIG_COUNTRIES;