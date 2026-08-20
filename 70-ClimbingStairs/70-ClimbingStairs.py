# Last updated: 8/20/2026, 2:18:50 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        a, b = 1, 2
        res = 0
        for _ in range(3, n+1):
            res = a + b
            a = b
            b = res

        return res

        

        