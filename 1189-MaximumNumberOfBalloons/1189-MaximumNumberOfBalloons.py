# Last updated: 10/7/2026, 2:59:39 PM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  
        
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        
        return res