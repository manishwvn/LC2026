# Last updated: 8/20/2026, 1:53:32 AM
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        diffs = [0] * (len(nums) + 1)

        for l, r in queries:
            diffs[l] += 1
            diffs[r+1] -=1

        for i in range(1, len(diffs)):
            diffs[i] += diffs[i-1]

        print(diffs)
        for i in range(len(nums)):
            if diffs[i] < nums[i]:
                return False
        
        return True