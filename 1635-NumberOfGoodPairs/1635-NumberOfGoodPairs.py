# Last updated: 8/20/2026, 2:02:01 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        hm = {}
        count = 0
        for num in nums:
            if num in hm:
                count += hm[num]
                hm[num] += 1
            else:
                hm[num] = 1
        return count