# Last updated: 8/20/2026, 1:54:20 AM
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        t_ind = {char: i for i, char in enumerate(t)}

        res = 0
        for i in range(len(s)):
            diff = abs(t_ind[s[i]] - i)
            res += diff

        return res
        