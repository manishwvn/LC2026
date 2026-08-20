# Last updated: 8/20/2026, 2:14:36 AM
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        empty = (2**31) - 1
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j])
                    
        while queue:
            r, c = queue.popleft()
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n or rooms[nr][nc] != empty:
                    continue
                
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append([nr, nc])
        
        