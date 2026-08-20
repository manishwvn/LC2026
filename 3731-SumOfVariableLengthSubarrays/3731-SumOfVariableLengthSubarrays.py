# Last updated: 8/20/2026, 1:53:15 AM
class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        res = 0
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res += prefix_sum[i+1] - prefix_sum[start]

        return res
        