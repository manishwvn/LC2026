# Last updated: 10/7/2026, 2:53:03 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:

        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""
        