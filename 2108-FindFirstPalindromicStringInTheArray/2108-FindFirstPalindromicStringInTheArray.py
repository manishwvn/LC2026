# Last updated: 10/7/2026, 2:51:11 PM
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            if word == word[::-1]:
                return word

        return ""
        