# Last updated: 8/20/2026, 2:18:45 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m * n - 1
        print(m, n)
        while l <= h:
            mid = (l + h) // 2

            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = mid - 1

            else:
                l = mid + 1

        return False
