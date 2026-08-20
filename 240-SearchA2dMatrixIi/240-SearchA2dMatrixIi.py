# Last updated: 8/20/2026, 2:15:03 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        r = 0
        c = n - 1
        
        while r < m and c > - 1:
            if target == matrix[r][c]:
                return True
            
            elif target <  matrix[r][c]:
                c -= 1
                
            else:
                 r += 1
            
        return False
                