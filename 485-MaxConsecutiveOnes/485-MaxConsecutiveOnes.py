# Last updated: 8/20/2026, 2:12:26 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        curr, maxm = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                curr = 0
            maxm = max(curr, maxm)

        return maxm