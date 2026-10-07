-- Last updated: 10/7/2026, 2:50:27 PM
select
    p.post_id as post_id,
    coalesce(group_concat(distinct k.topic_id order by k.topic_id), 'Ambiguous!') as topic
from
    posts p
left join
    keywords k
on
    concat(' ', lower(p.content), ' ')
    like concat('% ', lower(k.word), ' %')
group by
    p.post_id