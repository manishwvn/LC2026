# Last updated: 8/20/2026, 2:12:31 AM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        
        for i in range(1, length // 2 + 1):  # Check up to half the length
            if length % i == 0:  # Only check valid divisors
                if s[:i] * (length // i) == s:
                    return True
        
        return False