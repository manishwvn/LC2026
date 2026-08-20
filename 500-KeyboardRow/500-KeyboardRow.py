# Last updated: 8/20/2026, 2:12:15 AM
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        res = []

        for word in words:
            first = second = third = True
            for char in word:
                if char.lower() not in row1: first = False
                if char.lower() not in row2: second = False
                if char.lower() not in row3: third = False

            if first or second or third:
                res.append(word)

        return res
