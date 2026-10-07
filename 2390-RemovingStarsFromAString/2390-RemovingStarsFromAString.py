# Last updated: 10/7/2026, 2:49:19 PM
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


        