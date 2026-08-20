# Last updated: 8/20/2026, 2:07:27 AM
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
    
        j = 0
        i = 0
        n = len(name)
        t = len(typed)
        
        while j < t:
            if i < n and name[i] == typed[j]:
                i +=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j +=1
        return i == n