# Last updated: 10/7/2026, 2:42:35 PM
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        num_dict = Counter(nums)

        for num in nums:
            if num_dict[num] == 1 and num % 2 == 0:
                return num

        return -1

        