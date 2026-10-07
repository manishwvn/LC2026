-- Last updated: 10/7/2026, 2:54:26 PM
select
    date_id,
    make_name,
    count(distinct lead_id) as unique_leads,
    count(distinct partner_id) as unique_partners
from
    dailysales
group by
    date_id, make_name;