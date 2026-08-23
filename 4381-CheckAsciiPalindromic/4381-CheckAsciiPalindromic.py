# Last updated: 8/23/2026, 2:27:01 AM
class Solution:
    def isPalindromic(self, s: str) -> bool:

        binary = ''.join(format(ord(c), '08b') for c in s)
        return binary == binary[::-1]