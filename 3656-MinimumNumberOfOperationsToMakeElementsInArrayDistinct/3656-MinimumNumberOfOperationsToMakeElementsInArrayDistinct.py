# Last updated: 8/20/2026, 1:53:26 AM
class Solution:
    def minimumOperations(self, nums):
        seen = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0