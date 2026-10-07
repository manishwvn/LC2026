# Last updated: 10/7/2026, 2:49:23 PM
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        max_local = [[0] * (n-2) for _ in range(n-2)]

        for i in range(1, n-1):
            for j in range(1, n-1):
                max_val = 0

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        max_val = max(max_val, grid[i + di][j + dj])

                max_local[i-1][j-1] = max_val

        return max_local
