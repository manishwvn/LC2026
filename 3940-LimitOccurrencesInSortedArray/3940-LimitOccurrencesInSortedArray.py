# Last updated: 10/7/2026, 2:42:22 PM
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        if not nums:
            return []

        index = 0

        for num in nums:
            if index < k or num != nums[index - k]:
                nums[index] = num
                index += 1

        return nums[:index]

        