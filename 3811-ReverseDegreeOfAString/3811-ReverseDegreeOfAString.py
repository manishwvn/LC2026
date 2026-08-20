# Last updated: 8/20/2026, 1:53:03 AM
class Solution:
    def reverseDegree(self, s: str) -> int:

        res = 0
        for i, char in enumerate(s):
            rev = ord('z') - ord(char) + 1
            res += rev * (i+1)

        return res
        