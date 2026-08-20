# Last updated: 8/20/2026, 2:13:22 AM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = collections.Counter(s)

        for i in range(len(s)):
            if s[i] in hm and hm[s[i]] == 1:
                return i

        return -1