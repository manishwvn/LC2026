# Last updated: 10/7/2026, 3:04:08 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        result = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                result = min(k, result)
                r = k - 1
            else:
                l = k + 1
                    
        return result
                    
                
        