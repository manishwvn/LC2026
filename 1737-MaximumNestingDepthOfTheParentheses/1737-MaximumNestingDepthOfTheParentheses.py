# Last updated: 8/20/2026, 2:01:16 AM
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
        