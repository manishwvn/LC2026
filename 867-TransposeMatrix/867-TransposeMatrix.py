# Last updated: 10/7/2026, 3:04:10 PM
class Solution:
    def transpose(self, A):
        R = len(A)
        C = len(A[0])
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(A[r][c])
            transpose.append(newRow)
        return transpose