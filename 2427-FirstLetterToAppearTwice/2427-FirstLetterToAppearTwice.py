# Last updated: 8/20/2026, 1:57:08 AM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for char in s:
            if char in visited:
                return char
            visited.add(char)
        
        
        