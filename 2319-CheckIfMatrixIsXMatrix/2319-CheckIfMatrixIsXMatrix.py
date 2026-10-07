# Last updated: 10/7/2026, 2:49:56 PM
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        for i in range(len(grid)):
            for j in range(len(grid)):

                is_diagonal = False
                if i == j or j == len(grid) - i - 1:
                    is_diagonal = True

                if is_diagonal and grid[i][j] == 0:
                    return False

                if not is_diagonal and grid[i][j] != 0:
                    return False

        return True