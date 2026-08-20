# Last updated: 8/20/2026, 2:04:07 AM
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        if len(words) == 1:
            return words
        
        res = []
        prev_count = None
        
        for w in words:
            count = Counter(w)
            if prev_count != count:
                res.append(w)
                prev_count = count
                
        return res
        