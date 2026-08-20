# Last updated: 8/20/2026, 2:16:30 AM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        column = 0
        multiplier = 1
        
        for i in range(len(columnTitle) - 1, -1, -1):
            column += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *= 26
            
        return column
        