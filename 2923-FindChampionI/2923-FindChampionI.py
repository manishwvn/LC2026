# Last updated: 10/7/2026, 2:46:49 PM
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        n = len(grid)
        for i in range(n):
            is_champion = True
            for j in range(n):
                if i != j and grid[j][i] == 1:  # team j beats team i
                    is_champion = False
                    break
            if is_champion:
                return i