# Last updated: 8/20/2026, 2:02:16 AM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        if len(nums) <= 2: return nums

        ans = [0] * (2 * n)
        for i in range(n):
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[n + i]
        return ans


        