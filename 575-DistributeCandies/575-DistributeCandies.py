# Last updated: 8/20/2026, 2:11:16 AM
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        return min(len(set(candyType)), len(candyType) // 2)
        