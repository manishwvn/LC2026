# Last updated: 10/7/2026, 2:47:53 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left_sum, right_sum = 0, sum(nums)
        result = []
        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result
        