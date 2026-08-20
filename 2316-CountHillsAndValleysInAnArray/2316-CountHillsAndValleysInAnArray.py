# Last updated: 8/20/2026, 1:57:41 AM
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hillValley = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:     #hill check
                hillValley += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:     #valley check
                hillValley += 1
        return hillValley
        