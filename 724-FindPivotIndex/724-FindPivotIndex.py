# Last updated: 8/20/2026, 2:09:36 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - nums[i] - left
            if right == left:
                return i
            left += nums[i]
        return -1