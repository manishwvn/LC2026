# Last updated: 8/20/2026, 2:11:29 AM
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        sum_ = 0
        for i in range(1, len(nums), 2):
            sum_ += min(nums[i-1], nums[i])
            
        return sum_
        