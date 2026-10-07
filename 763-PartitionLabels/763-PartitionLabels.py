# Last updated: 10/7/2026, 3:05:44 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        if not s or len(s) == 0: return []
        
        result = []
        
        hm = {char:index for index, char in enumerate(s)}
        
        start, end = 0, 0
        
        for i in range(len(s)):
            char = s[i]
            end = max(end, hm[char])
            
            if i == end:
                result.append(end - start + 1)
                start = i + 1
                
        return result
        
        
        