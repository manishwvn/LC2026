# Last updated: 10/7/2026, 3:03:05 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for k in (1, 2, 3):
                if i + k < n and nums[i] == nums[i + k]:
                    return nums[i]