# Last updated: 8/20/2026, 2:15:03 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return True if Counter(s) == Counter(t) else False
        