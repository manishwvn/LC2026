# Last updated: 10/7/2026, 2:55:14 PM
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
        