# Last updated: 10/7/2026, 2:58:40 PM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod, sumn = 1, 0
        
        while n:
            rem = n % 10
            sumn += rem
            prod *= rem
            n //= 10
            
        return prod - sumn
        