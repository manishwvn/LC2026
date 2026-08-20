# Last updated: 8/20/2026, 2:15:37 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_set = set(nums)

        return False if len(num_set) == len(nums) else True
        