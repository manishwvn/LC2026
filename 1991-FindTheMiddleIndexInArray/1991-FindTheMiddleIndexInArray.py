# Last updated: 10/7/2026, 2:52:28 PM
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
        