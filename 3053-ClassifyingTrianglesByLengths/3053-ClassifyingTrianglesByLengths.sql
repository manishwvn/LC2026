-- Last updated: 10/7/2026, 2:46:27 PM
select
    case
        when a + b > c and b + c > a and a + c > b then (
            case
                when
                    a = b and b = c then 'Equilateral'
                when
                    a = b or b = c or c = a then 'Isosceles'
                else
                    'Scalene'
            end

        )
        else 'Not A Triangle' end as triangle_type
from
    triangles;