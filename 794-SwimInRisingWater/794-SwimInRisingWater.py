# Last updated: 8/20/2026, 2:08:56 AM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        visited = set()
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        heap = [[grid[0][0], 0, 0]]
        visited.add((0, 0))
        
        while heap:
            
            time, r, c = heappop(heap)
            
            if r == n-1 and c == n-1:
                return time
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if (0 <= nr < n) and (0 <= nc < n) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heappush(heap, [max(time, grid[nr][nc]), nr, nc])
                    
        
        
        
        