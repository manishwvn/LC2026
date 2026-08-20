# Last updated: 8/20/2026, 2:04:54 AM
class Solution:
    def dayOfYear(self, date: str) -> int:

        def leap(year):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False


        year, month, day = [int(x) for x in date.split("-")]

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap(year):
            days_in_month[1] = 29
        
        day_of_year = sum(days_in_month[:month - 1]) + day
        
        return day_of_year



        
        
        