# Last updated: 8/20/2026, 2:14:47 AM
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        chars = set()

        for char in s:
            if char in chars:
                chars.remove(char)
            else:
                chars.add(char)
        return len(chars) <= 1
        