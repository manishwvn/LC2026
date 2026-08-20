# Last updated: 8/20/2026, 1:59:45 AM
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [(w[-1], w[:-1]) for w in s.split(" ")]
        arr.sort()
        return " ".join([w for i, w in arr])
