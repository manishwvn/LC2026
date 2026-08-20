# Last updated: 8/20/2026, 1:56:17 AM
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = (n * (n + 1)) // 2
        x = math.isqrt(total_sum)
        
        # Returns x if an exact integer pivot exists, else -1
        return x if x * x == total_sum else -1