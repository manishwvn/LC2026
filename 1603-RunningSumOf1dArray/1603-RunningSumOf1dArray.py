# Last updated: 8/20/2026, 2:02:13 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        for i in range(1, len(nums)):
            nums[i] = nums[i] +nums[i-1]
        return nums