# Last updated: 8/20/2026, 1:52:51 AM
class Solution:
    def maxProduct(self, n: int) -> int:

        a, b = float("-inf"), float("-inf")

        while n:
            rem = n % 10

            if rem > a:
                b = a
                a = rem
            elif rem > b:
                b = rem
            n //= 10

        print(a)
        print(b)
        return a * b

        