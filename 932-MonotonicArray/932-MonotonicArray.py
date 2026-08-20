# Last updated: 8/20/2026, 2:07:37 AM
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        is_inc, is_dec = True, True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                is_inc = False
            if nums[i] < nums[i+1]:
                    is_dec = False
        
        return is_inc or is_dec

        