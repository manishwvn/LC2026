# Last updated: 10/7/2026, 2:54:52 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed_set = set(chr for chr in allowed)
        count = 0

        for word in words:
            if all(char in allowed_set for char in word):
                count += 1

        return count
        