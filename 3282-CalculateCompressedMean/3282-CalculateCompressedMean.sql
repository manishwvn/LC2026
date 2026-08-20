-- Last updated: 8/20/2026, 1:54:55 AM
select
    round(ifnull(sum(item_count * order_occurrences) / sum(order_occurrences), 0), 2)
    as average_items_per_order
from
    orders;