# Last updated: 8/20/2026, 1:52:22 AM
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        num_dict = Counter(nums)

        for num in nums:
            if num_dict[num] == 1 and num % 2 == 0:
                return num

        return -1

        