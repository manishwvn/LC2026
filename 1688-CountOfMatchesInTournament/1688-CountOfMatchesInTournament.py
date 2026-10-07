# Last updated: 10/7/2026, 2:54:42 PM
class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        
        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                print("teams is even", n)
                n //= 2
                
            else:
                matches += (n-1) // 2
                print("teams is odd", n)
                n = ((n - 1) // 2) + 1
                
        return matches