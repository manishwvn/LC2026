# Last updated: 8/20/2026, 2:17:37 AM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        for row in range(1, len(triangle)):
            for col in range(row+1):
                min_val = float("inf")
                
                if col > 0:
                    min_val = triangle[row - 1][col - 1]
                    
                if col < row:
                    min_val = min(min_val, triangle[row-1][col])
                    
                triangle[row][col] += min_val
                
        return min(triangle[-1])
                
        