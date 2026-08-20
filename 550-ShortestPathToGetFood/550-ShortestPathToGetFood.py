# Last updated: 8/20/2026, 2:11:36 AM
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        queue = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    heappush(queue, [0, i, j])
                    visited.add((i, j))
                    break
        
        
        while queue:
            steps, r, c = heappop(queue)
            
            if grid[r][c] == "#":
                return steps
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != "X":
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heappush(queue, [steps+1, nr, nc])
                        
        return -1
            
                    
        
        