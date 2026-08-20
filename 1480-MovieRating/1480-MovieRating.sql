-- Last updated: 8/20/2026, 2:03:11 AM
with cte as (select
    u.user_id,
    u.name,
    count(mr.rating) as ratings,
    dense_rank() over(order by count(mr.rating) desc, u.name asc) as rnk
from
    users u
join
    movierating mr
on
    u.user_id = mr.user_id
group by
    u.user_id,
    u.name),

cte2 as (
    select
        m.movie_id,
        m.title,
        avg(mr.rating) as avg_movie_rating,
        dense_rank() over(order by avg(mr.rating) desc, m.title asc) as rnk
    from
        movierating mr
    join
        movies m
    on
        mr.movie_id = m.movie_id
    where
        year(mr.created_at) = 2020 and month(mr.created_at) = 2
    group by
        movie_id)


select
    name as results
from
    cte
where
    rnk = 1
union all
select
    title
from
    cte2
where
    rnk = 1