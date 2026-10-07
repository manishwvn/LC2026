# Last updated: 10/7/2026, 2:48:34 PM
class Solution:
    def numberOfCuts(self, n: int) -> int:
        
        if n == 1: return 0
        if n % 2 != 0:
            return n
        else:
            return n // 2