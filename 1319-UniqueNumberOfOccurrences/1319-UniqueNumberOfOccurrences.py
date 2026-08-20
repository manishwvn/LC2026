# Last updated: 8/20/2026, 2:04:16 AM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts, checks = Counter(arr), set()
        
        if len(set(counts.values())) != len(counts):
            return False
        
        return True
        
        
        