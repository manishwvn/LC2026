# Last updated: 10/7/2026, 3:04:00 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        start, end = 0, len(people) - 1
        result = 0
        
        while start <= end:
            result += 1
            
            if people[start] + people[end] <= limit:
                start += 1
            
            end -= 1
            
        return result
            
        