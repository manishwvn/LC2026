-- Last updated: 8/20/2026, 2:10:29 AM
update Salary
set sex = 
    case when sex =  'm' then 'f'
    else 'm'
    end;