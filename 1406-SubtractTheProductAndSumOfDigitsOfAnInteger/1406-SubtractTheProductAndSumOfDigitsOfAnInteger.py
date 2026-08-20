# Last updated: 8/20/2026, 2:03:46 AM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod, sumn = 1, 0
        
        while n:
            rem = n % 10
            sumn += rem
            prod *= rem
            n //= 10
            
        return prod - sumn
        