# Last updated: 8/20/2026, 2:16:48 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        minm, maxm = nums[0], nums[0]
        result = maxm
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, maxm*curr, minm*curr)
            minm = min(curr, maxm*curr, minm*curr)
            maxm = temp_max
            
            result = max(maxm, result)
            
        return result
        
        