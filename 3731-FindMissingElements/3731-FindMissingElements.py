# Last updated: 10/7/2026, 2:42:49 PM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        minm, maxm = min(nums), max(nums)
        num_set = set(nums)
        res = []
        for num in range(minm, maxm+1):
            if num not in num_set:
                res.append(num)

        return res

        