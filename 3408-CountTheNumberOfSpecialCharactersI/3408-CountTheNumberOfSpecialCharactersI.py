# Last updated: 8/20/2026, 1:54:21 AM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers, uppers, special = set(), set(), set()

        for char in word:
            if 'a' <= char <= 'z':
                lowers.add(char)
                if char.upper() in uppers:
                    special.add(char)

            else:
                uppers.add(char)
                if char.lower() in lowers:
                    special.add(char.lower())

        return len(special)