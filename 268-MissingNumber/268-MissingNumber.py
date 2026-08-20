# Last updated: 8/20/2026, 2:14:46 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        sum_ = sum(nums)

        return ((n * (n+1)) // 2) - sum_
        