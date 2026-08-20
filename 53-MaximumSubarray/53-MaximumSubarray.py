# Last updated: 8/20/2026, 2:19:17 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        maxsub = nums[0]
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxsub = max(maxsub, curr)
        return maxsub
        