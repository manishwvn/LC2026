# Last updated: 10/7/2026, 2:41:57 PM
class Solution:
    def isPalindromic(self, s: str) -> bool:

        binary = ''.join(format(ord(c), '08b') for c in s)
        return binary == binary[::-1]