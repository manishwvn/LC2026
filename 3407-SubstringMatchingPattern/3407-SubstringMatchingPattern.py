# Last updated: 10/7/2026, 2:44:05 PM
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split("*")
        Len1, Len2 = len(p[0]), len(p[1])
        for i in range(len(s) - Len1 - Len2 + 1):
            if s[i:i+Len1] == p[0]:
                for j in range(i+Len1, len(s) - Len2 + 1):
                    if s[j:j+Len2] == p[1]:
                        return True
        return False