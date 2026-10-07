# Last updated: 10/7/2026, 2:49:08 PM
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
        
        
        
        
        