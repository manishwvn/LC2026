# Last updated: 8/20/2026, 2:02:02 AM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = (high - low) // 2

        if low % 2 != 0 or high % 2 != 0:
            odd += 1

        return odd
        