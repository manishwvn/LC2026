# Last updated: 8/20/2026, 2:18:18 AM
class Solution:
    def numDecodings(self, s: str) -> int:

        if not s: return 0
        
        prev1 = 1 if s[-1] != '0' else 0
        prev2 = 1

        for i in range(len(s)-2, -1, -1):
            curr = 0
            if s[i] == '0':
                curr = 0
            else:
                #1 digit
                curr += prev1

                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    curr += prev2
            prev2, prev1 = prev1, curr

        return prev1
        