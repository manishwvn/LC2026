# Last updated: 10/7/2026, 3:04:20 PM
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        while (p%2==0 and q%2==0): 
            p = p / 2
            q = q / 2
	
	
	
        if (p%2 == 0):
            return 2

        if (q%2 == 0):
            return 0

        return 1
        
        