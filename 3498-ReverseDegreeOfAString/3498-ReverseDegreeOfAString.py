# Last updated: 10/7/2026, 2:43:36 PM
class Solution:
    def reverseDegree(self, s: str) -> int:

        res = 0
        for i, char in enumerate(s):
            rev = ord('z') - ord(char) + 1
            res += rev * (i+1)

        return res
        