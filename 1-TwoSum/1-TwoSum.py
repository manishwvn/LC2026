# Last updated: 8/20/2026, 2:20:48 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hm:
                return [i, hm[diff]]

            hm[nums[i]] = i

        return []
        