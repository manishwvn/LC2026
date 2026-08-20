# Last updated: 8/20/2026, 2:20:37 AM
class Solution:
    def reverse(self, x: int) -> int:

        sign = 1 if x > 0 else -1
        revx, x = 0, abs(x)

        while x:
            mod = x % 10
            revx = revx * 10 + mod
            x //= 10

        return sign * revx if revx < 2 ** 31 - 1 else 0
        