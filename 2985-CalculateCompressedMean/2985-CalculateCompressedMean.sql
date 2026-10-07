-- Last updated: 10/7/2026, 2:46:24 PM
select
    round(ifnull(sum(item_count * order_occurrences) / sum(order_occurrences), 0), 2)
    as average_items_per_order
from
    orders;