# Last updated: 8/20/2026, 2:09:07 AM
from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counts = Counter(s)
        heap = []
        
        for char, freq in counts.items():
            heappush(heap, [-freq, char])
            
        result = ""
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""
            
            count, char = heappop(heap)
            result += char
            count += 1
            
            if prev:
                heappush(heap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]
        
        return result
        