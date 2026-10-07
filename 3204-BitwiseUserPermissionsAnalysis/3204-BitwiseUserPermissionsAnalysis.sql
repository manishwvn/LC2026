-- Last updated: 10/7/2026, 2:45:08 PM
select
    bit_and(permissions) as common_perms,
    bit_or(permissions) as any_perms
from
    user_permissions;