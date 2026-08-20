# Last updated: 8/20/2026, 1:55:13 AM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        res = []

        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
        