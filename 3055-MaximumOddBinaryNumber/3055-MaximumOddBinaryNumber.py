# Last updated: 8/20/2026, 1:55:27 AM
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt1 = s.count('1')
        cnt0 = s.count('0')
        ans = '1' * (cnt1 - 1) + '0' * cnt0 + '1'
        return ans
