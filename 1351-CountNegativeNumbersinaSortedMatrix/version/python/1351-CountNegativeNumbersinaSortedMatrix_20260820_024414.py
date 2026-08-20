# Last updated: 8/20/2026, 2:44:14 AM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        
4        count = 0
5        for row in grid:
6            for num in row:
7                if num < 0:
8                    count += 1
9        return count