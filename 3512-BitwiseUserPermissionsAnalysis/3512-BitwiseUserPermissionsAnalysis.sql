-- Last updated: 8/20/2026, 1:54:02 AM
select
    bit_and(permissions) as common_perms,
    bit_or(permissions) as any_perms
from
    user_permissions;