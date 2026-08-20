# Last updated: 8/20/2026, 2:09:52 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)
            i += 1
            j -= 1
        
        return True