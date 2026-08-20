# Last updated: 8/20/2026, 2:02:42 AM
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result