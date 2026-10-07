# Last updated: 10/7/2026, 2:55:23 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth, curr = 0, 0 
        
        for char in s:
            if char == "(":
                curr += 1
                depth = max(depth, curr)
                
            elif char == ")":
                curr -= 1
                
        return depth
        