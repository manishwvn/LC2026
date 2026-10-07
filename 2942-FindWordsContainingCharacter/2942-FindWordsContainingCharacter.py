# Last updated: 10/7/2026, 2:46:47 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        res = []

        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
        