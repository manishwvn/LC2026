# Last updated: 8/20/2026, 2:00:52 AM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed_set = set(chr for chr in allowed)
        count = 0

        for word in words:
            if all(char in allowed_set for char in word):
                count += 1

        return count
        