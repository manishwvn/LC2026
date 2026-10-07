# Last updated: 10/7/2026, 2:53:47 PM
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        
        if c[0] in "aceg":
            return int(c[1]) % 2 == 0
        if c[0] in "bdfh":
            return int(c[1]) % 2 == 1
        