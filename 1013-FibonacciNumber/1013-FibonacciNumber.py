# Last updated: 8/20/2026, 2:07:07 AM
class Solution:
    def fib(self, n: int) -> int:

        if n <=1: return n

        result, a, b = 0, 0, 1

        for i in range(2, n+1):
            result = a + b
            a = b
            b = result
        
        return result



        