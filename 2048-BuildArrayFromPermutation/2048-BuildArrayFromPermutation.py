# Last updated: 8/20/2026, 1:59:20 AM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n

        for i in range(n):
            nums[i] //= n

        return nums