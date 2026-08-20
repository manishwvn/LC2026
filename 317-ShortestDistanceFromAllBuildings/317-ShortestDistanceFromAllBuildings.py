# Last updated: 8/20/2026, 2:14:12 AM
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
        m, n = len(grid), len(grid[0])
        total = [[0 for _ in range(n)] for _ in range(m)]
        min_dist = float('inf')
        empty = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_dist = float("inf")
                    queue = deque()

                    queue.append((i, j))

                    steps = 0

                    while queue:
                        steps += 1

                        for _ in range(len(queue)):
                            r, c = queue.popleft()

                            for dir in dirs:
                                x = r + dir[0]
                                y = c + dir[1]

                                if 0 <= x < m and 0 <= y < n and grid[x][y] == empty:
                                    grid[x][y] -= 1
                                    total[x][y] += steps
                                    queue.append((x, y))

                                    min_dist = min(min_dist, total[x][y])
                    empty -= 1
        return min_dist if min_dist != float('inf') else -1
        