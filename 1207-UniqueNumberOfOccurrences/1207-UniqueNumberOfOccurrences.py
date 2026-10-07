# Last updated: 10/7/2026, 2:59:19 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts, checks = Counter(arr), set()
        
        if len(set(counts.values())) != len(counts):
            return False
        
        return True
        
        
        