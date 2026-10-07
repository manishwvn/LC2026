# Last updated: 10/7/2026, 2:56:09 PM
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        shuffled = [None] * len(s)

        for i in range(len(s)):
            shuffled[indices[i]] = s[i]

        return ''.join(shuffled)

        