# Last updated: 8/20/2026, 2:01:13 AM
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = {}
        res = -1

        for i, char in enumerate(s):
            if char in hm:
                res = max(res, i - hm[char] - 1)
            else:
                hm[char] = i

        return res
        