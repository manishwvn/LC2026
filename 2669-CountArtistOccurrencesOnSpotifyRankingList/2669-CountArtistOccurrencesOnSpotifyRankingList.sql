-- Last updated: 10/7/2026, 2:47:37 PM
select
    artist,
    count(artist) as occurrences
from
    spotify
group by
    artist
order by
    2 desc, 1 asc;