# Last updated: 8/20/2026, 1:56:37 AM
class Solution:
    def partitionString(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        char_count, sub_count  = set(), 1
        
        for i in range(len(s)):
            if s[i] not in char_count:
                char_count.add(s[i])
                
            else:
                char_count = set()
                char_count.add(s[i])
                sub_count += 1
                
                
        return sub_count
        
        
        
        
        