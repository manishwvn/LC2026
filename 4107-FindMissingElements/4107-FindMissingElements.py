# Last updated: 8/20/2026, 1:52:33 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        minm, maxm = min(nums), max(nums)
        num_set = set(nums)
        res = []
        for num in range(minm, maxm+1):
            if num not in num_set:
                res.append(num)

        return res

        