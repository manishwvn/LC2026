# Last updated: 8/20/2026, 1:54:41 AM
class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            if s[i].lower() != s[i + 1].lower():
                res += 1
        return res