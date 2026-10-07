# Last updated: 10/7/2026, 3:05:12 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        return goal in s + s
        
        
        