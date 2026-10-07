# Last updated: 10/7/2026, 2:45:33 PM
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        t_ind = {char: i for i, char in enumerate(t)}

        res = 0
        for i in range(len(s)):
            diff = abs(t_ind[s[i]] - i)
            res += diff

        return res
        