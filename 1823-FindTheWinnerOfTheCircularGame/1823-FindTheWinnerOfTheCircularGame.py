# Last updated: 10/7/2026, 2:53:33 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        res = 0
        
        for i in range(1, n+1):
            res = (res + k) % i
            
        return res + 1
        