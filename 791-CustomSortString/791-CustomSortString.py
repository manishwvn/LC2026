# Last updated: 10/7/2026, 3:05:18 PM
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
                
        