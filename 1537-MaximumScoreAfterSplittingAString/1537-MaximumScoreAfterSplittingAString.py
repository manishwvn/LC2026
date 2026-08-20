# Last updated: 8/20/2026, 2:02:36 AM
class Solution:
    def maxScore(self, s: str) -> int:

        zero = 0
        one = s.count('1')
        result = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            
            result = max(result, one + zero)
        
        return result
        