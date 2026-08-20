# Last updated: 8/20/2026, 2:08:50 AM
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counts = Counter(s)
        res = ""
        
        # print(counts)
        for char in order:
            if char in counts:
                res = res + (counts[char] * char)
                del counts[char]
        
        # print(res)
        
        for key, val in counts.items():
            res = res + (key * val)
                
        return res
                
        