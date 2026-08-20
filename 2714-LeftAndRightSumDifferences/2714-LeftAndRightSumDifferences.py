# Last updated: 8/20/2026, 1:55:55 AM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left_sum, right_sum = 0, sum(nums)
        result = []
        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result
        