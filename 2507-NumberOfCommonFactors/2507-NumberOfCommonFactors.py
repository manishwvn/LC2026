# Last updated: 8/20/2026, 1:56:32 AM
class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        count = 0
        for i in range(1, min(a,b)+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count