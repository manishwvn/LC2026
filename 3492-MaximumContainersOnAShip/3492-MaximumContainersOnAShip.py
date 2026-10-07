# Last updated: 10/7/2026, 2:43:31 PM
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        res = 0
        for i in range(1, n*n+1):
            if(w*i <= maxWeight):
                res = max(res, i)
        return res
                