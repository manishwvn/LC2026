# Last updated: 10/7/2026, 2:53:26 PM
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [(w[-1], w[:-1]) for w in s.split(" ")]
        arr.sort()
        return " ".join([w for i, w in arr])
