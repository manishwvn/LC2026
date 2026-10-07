-- Last updated: 10/7/2026, 2:44:00 PM
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