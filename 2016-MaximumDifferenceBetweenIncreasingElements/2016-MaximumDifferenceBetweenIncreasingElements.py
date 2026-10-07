# Last updated: 10/7/2026, 2:52:03 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        diff = -1
        minm = float('inf')

        for num in nums:
            if num <= minm:
                minm = num
            else:
                diff = max(diff, num - minm)

        return diff

        