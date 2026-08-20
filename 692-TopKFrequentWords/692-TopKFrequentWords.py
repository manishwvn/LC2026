# Last updated: 8/20/2026, 2:09:48 AM
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counts = Counter(words)
        heap = []
        
        print(counts)
        for key, val in counts.items():
            heappush(heap, [-val, key])
                
        return [heappop(heap)[1] for _ in range(k)]
            
        
        
        
        