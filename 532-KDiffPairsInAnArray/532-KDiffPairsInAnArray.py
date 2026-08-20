# Last updated: 8/20/2026, 2:11:50 AM
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hm = Counter(nums)
        res = 0
        
        for key in hm:
            if k > 0 and key + k in hm:
                res += 1
                
            elif k == 0 and hm[key] > 1:
                res += 1
                
        return res
        
        