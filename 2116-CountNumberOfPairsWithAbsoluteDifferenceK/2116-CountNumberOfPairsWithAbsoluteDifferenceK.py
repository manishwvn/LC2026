# Last updated: 8/20/2026, 1:58:57 AM
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hm = collections.Counter(nums)
        count = 0
        for num in nums:
            if num + k in hm:
                count += hm[num + k]
                
        return count
        