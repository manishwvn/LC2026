# Last updated: 10/7/2026, 2:43:59 PM
class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        total = sum(nums)
        left_sum = 0
        right_sum = 0
        parts = 0

        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if abs(left_sum - right_sum) % 2 == 0:
                parts += 1

        return parts