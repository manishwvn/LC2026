# Last updated: 8/20/2026, 1:56:47 AM
class Solution:
    def removeStars(self, s: str) -> str:

        l = 0
        chars = list(s)
        for r in range(len(s)):

            if s[r] != '*':
                chars[l] = s[r]
                l += 1

            else:
                if l > 0:
                    l -= 1

        return "".join(chars[:l])


        