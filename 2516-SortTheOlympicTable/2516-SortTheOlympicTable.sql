-- Last updated: 8/20/2026, 1:56:29 AM
select 
    country,
    gold_medals,
    silver_medals,
    bronze_medals
from 
    Olympic
order by 
    gold_medals desc,
    silver_medals desc,
    bronze_medals desc,
    country;