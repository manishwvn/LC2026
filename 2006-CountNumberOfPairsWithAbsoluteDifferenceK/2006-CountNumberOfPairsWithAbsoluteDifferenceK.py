# Last updated: 10/7/2026, 2:52:21 PM
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hm = collections.Counter(nums)
        count = 0
        for num in nums:
            if num + k in hm:
                count += hm[num + k]
                
        return count
        