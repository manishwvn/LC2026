# Last updated: 8/20/2026, 1:52:24 AM
class Solution:
    def firstMatchingIndex(self, s: str) -> int:

        for i in range(len(s)):
            if s[i] == s[len(s) - i - 1]:
                return i

        return -1