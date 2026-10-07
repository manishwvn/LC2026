# Last updated: 10/7/2026, 2:48:04 PM
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])
        res = [0] * n
        for col in range(n):
            for row in range(m):
                val = grid[row][col]

                sign = 0
                if val < 0:
                    sign = 1
                
                val = abs(val)
                digits = 1
                while val >= 10:
                    val //= 10
                    digits += 1

                res[col] = max(res[col], digits + sign)

        return res