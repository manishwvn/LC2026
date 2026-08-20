# Last updated: 8/20/2026, 2:10:15 AM
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def count_pal(string, l, r):
            result = 0
            
            while l >= 0 and r < len(string) and string[l] == string[r]:
                result += 1
                l -= 1
                r += 1
                
            return result
        
        result = 0
        
        for i in range(len(s)):
            result += count_pal(s, i, i+1)
            result += count_pal(s, i, i)
            
        return result
        