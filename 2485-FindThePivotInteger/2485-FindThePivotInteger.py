# Last updated: 10/7/2026, 2:48:35 PM
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = (n * (n + 1)) // 2
        x = math.isqrt(total_sum)
        
        # Returns x if an exact integer pivot exists, else -1
        return x if x * x == total_sum else -1