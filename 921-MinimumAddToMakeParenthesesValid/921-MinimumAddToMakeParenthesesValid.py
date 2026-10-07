# Last updated: 10/7/2026, 3:03:31 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        opens = 0
        res = 0

        for char in s:
            if char == "(":
                opens += 1
            else:
                if opens:
                    opens -= 1
                else:
                    res += 1
        return res + opens
        