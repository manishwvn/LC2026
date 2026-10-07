# Last updated: 10/7/2026, 2:46:06 PM
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        steps = 0
        res = 0
        for num in nums:
            steps += num
            if steps == 0:
                res += 1

        return res