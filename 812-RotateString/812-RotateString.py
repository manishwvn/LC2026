# Last updated: 8/20/2026, 2:08:45 AM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        return goal in s + s
        
        
        