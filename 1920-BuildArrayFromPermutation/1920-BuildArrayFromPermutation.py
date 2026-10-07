# Last updated: 10/7/2026, 2:52:50 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n

        for i in range(n):
            nums[i] //= n

        return nums