-- Last updated: 8/20/2026, 2:00:31 AM
select
    date_id,
    make_name,
    count(distinct lead_id) as unique_leads,
    count(distinct partner_id) as unique_partners
from
    dailysales
group by
    date_id, make_name;