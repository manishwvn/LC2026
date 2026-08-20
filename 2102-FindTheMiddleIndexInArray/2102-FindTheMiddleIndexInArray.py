# Last updated: 8/20/2026, 1:59:03 AM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1
        