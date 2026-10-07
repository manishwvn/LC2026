# Last updated: 10/7/2026, 2:42:32 PM
class Solution:
    def firstMatchingIndex(self, s: str) -> int:

        for i in range(len(s)):
            if s[i] == s[len(s) - i - 1]:
                return i

        return -1