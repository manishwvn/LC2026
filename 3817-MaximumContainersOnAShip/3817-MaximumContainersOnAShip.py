# Last updated: 8/20/2026, 1:53:01 AM
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        res = 0
        for i in range(1, n*n+1):
            if(w*i <= maxWeight):
                res = max(res, i)
        return res
                