# Last updated: 10/7/2026, 3:02:55 PM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0
        