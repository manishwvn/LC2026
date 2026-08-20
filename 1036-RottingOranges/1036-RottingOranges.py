# Last updated: 8/20/2026, 2:06:50 AM
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0: return 0
        
        time = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        if fresh == 0:
                            return time + 1
                        queue.append((nx, ny))
            time += 1
        
        return -1 if fresh else time