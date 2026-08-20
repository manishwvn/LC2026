# Last updated: 8/20/2026, 2:04:33 AM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  
        
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        
        return res