# Last updated: 8/20/2026, 2:13:56 AM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # if n == 1: return True
        # if n <= 0 or n % 4: return False

        # return self.isPowerOfFour(n // 4)

        # while n:
        #     if n == 1: return True
        #     if n <= 0 or n % 4: return False
        #     n //= 4

        # return False
        
        return n > 0 and log(n, 4) % 1 == 0