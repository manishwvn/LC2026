# Last updated: 8/20/2026, 1:57:26 AM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        n = len(nums)
        left_sum = 0
        right_sum = 0

        for num in nums:
            right_sum += num

        counts = 0
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]

            if left_sum >= right_sum:
                counts += 1
        return counts
