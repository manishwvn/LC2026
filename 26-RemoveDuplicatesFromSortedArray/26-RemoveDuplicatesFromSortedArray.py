# Last updated: 8/20/2026, 2:20:02 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                 nums[l] = nums[r]
                 l += 1
            r += 1

        return l 