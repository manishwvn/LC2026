-- Last updated: 8/20/2026, 1:55:48 AM
select
    artist,
    count(artist) as occurrences
from
    spotify
group by
    artist
order by
    2 desc, 1 asc;