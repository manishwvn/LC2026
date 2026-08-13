# Last updated: 8/13/2026, 12:45:25 AM
1class Solution:
2    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
3        n = len(nums) - 2
4        sum_ = sum(nums)
5        squared_sum = sum(x * x for x in nums)
6        sum2 = sum_ - n * (n - 1) // 2
7        squared_sum2 = squared_sum - n * (n - 1) * (2 * n - 1) // 6
8        x1 = (sum2 - math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
9        x2 = (sum2 + math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
10        return [int(x1), int(x2)]