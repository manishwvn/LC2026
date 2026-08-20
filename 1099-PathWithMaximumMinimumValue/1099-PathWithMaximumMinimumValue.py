# Last updated: 8/20/2026, 2:06:28 AM
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = []
        heappush(queue, [-grid[0][0], 0, 0])
        visited = set()
        visited.add((0, 0))
        
        while queue:
            value, r, c = heappop(queue)
            
            
            if r == m - 1 and c == n - 1:
                return -value
            
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heappush(queue, [max(value, -grid[nr][nc]), nr, nc])
                        
                        
        return -1
        
            
            
            
            
        
        