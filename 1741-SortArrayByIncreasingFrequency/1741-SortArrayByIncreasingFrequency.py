# Last updated: 8/20/2026, 2:01:14 AM
from heapq import *
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        heap = []
    
        for key, val in counts.items():
            heappush(heap, [val, -key])
            
        result = []
        while heap:
            val, key = heappop(heap)
            key = -key
            
            for _ in range(val):
                result.append(key)
            
        return result
            
            
            
            
        
        