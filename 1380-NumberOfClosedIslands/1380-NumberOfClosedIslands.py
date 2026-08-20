# Last updated: 8/20/2026, 2:04:00 AM
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(i, j):
            queue = deque()
            queue.append([i, j])
            visited.add((i, j))
            closed = True

            while queue:
                x, y = queue.popleft()

                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    closed = False

                for dir in dirs:
                    nx, ny = x + dir[0], y + dir[1]

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        queue.append([nx, ny])
                        visited.add((nx, ny))
            
            return closed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if bfs(i, j):
                        count += 1
        return count
        