-- Last updated: 10/7/2026, 2:48:57 PM
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