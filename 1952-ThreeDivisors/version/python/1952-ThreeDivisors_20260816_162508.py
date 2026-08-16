# Last updated: 8/16/2026, 4:25:08 PM
1class Solution:
2    def isThree(self, n: int) -> bool:
3        # Step 1: Find the integer square root
4        root = int(n**0.5)
5        
6        # Must be a perfect square greater than 1 (since root >= 2 for primes)
7        if root * root != n or root < 2:
8            return False
9            
10        # Step 2: Check if root is a prime number
11        for i in range(2, int(root**0.5) + 1):
12            if root % i == 0:
13                return False  # root is composite, so n has > 3 divisors
14                
15        return True