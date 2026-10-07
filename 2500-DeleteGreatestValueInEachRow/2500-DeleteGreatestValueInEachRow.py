# Last updated: 10/7/2026, 2:48:25 PM
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            grid[i].sort()

        for j in range(n):
            max_in_col = 0
            for i in range(m):
                max_in_col = max(max_in_col, grid[i][j])
            res += max_in_col

        return res
        