# Last updated: 8/20/2026, 1:59:50 AM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        res = 0
        
        for i in range(1, n+1):
            res = (res + k) % i
            
        return res + 1
        