# Last updated: 8/20/2026, 2:03:26 AM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count, left = 0, 0
        map = {x:0 for x in "abc"}
        
        for right in range(0,len(s)):
            map[s[right]] += 1
            
            while map["a"] and map["b"] and map["c"]:
                map[s[left]] -= 1
                left += 1
            
            count += left
            
        return count