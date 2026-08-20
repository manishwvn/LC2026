# Last updated: 8/20/2026, 2:12:54 AM
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            col = ""
            for j in range(len(words)):
                if i < len(words[j]):
                    col += words[j][i]
            if words[i] != col:
                return False

        return True

