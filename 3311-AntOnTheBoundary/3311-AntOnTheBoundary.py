# Last updated: 8/20/2026, 1:54:43 AM
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        steps = 0
        res = 0
        for num in nums:
            steps += num
            if steps == 0:
                res += 1

        return res