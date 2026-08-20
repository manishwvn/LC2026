# Last updated: 8/20/2026, 2:01:53 AM
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        shuffled = [None] * len(s)

        for i in range(len(s)):
            shuffled[indices[i]] = s[i]

        return ''.join(shuffled)

        