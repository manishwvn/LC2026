# Last updated: 8/20/2026, 2:11:27 AM
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        res = []
        for i in range(r):
            row = []
            for j in range(c):
                idx = i * c + j
                old_row = idx // n
                old_col = idx % n
                row.append(mat[old_row][old_col])
            res.append(row)

        return res