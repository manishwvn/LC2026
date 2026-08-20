# Last updated: 8/20/2026, 2:19:07 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

        