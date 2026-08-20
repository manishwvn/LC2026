# Last updated: 8/20/2026, 1:59:25 AM
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        large_1, large_2 = -float('inf'), -float('inf')
        small_1, small_2 = float('inf'), float('inf')

        for num in nums:
            if num > large_1:
                large_2 = large_1
                large_1 = num

            elif num > large_2:
                large_2 = num

            if num < small_1:
                small_2 = small_1
                small_1 = num
            elif num < small_2:
                small_2 = num

        return (large_1 * large_2) - (small_1 * small_2)