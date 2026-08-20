# Last updated: 8/20/2026, 2:00:11 AM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = j = 0
        m, n = len(word1), len(word2)

        while i < m or j < n:
            if i < m:
                result = result + word1[i]
                i += 1
            if j < n:
                result = result + word2[j]
                j += 1

        return result