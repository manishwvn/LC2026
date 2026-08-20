# Last updated: 8/20/2026, 2:01:06 AM
from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                continue
                
            heappush(heap, diff)
            
            if len(heap) <= ladders:
                continue
                
            bricks -= heappop(heap)
            
            if bricks < 0:
                return i
            
        return len(heights) - 1
        