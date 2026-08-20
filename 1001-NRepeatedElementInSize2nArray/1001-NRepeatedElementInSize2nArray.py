# Last updated: 8/20/2026, 2:07:10 AM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for k in (1, 2, 3):
                if i + k < n and nums[i] == nums[i + k]:
                    return nums[i]