-- Last updated: 8/20/2026, 1:53:20 AM
select
    book_id,
    title,
    author,
    published_year
from
    books
where rating is NULL
order by
    book_id;