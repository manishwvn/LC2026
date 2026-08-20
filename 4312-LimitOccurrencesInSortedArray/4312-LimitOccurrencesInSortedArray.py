# Last updated: 8/20/2026, 1:52:10 AM
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

        