# Last updated: 10/7/2026, 2:47:42 PM
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        best_idx, best_count = 0, -1

        for i, row in enumerate(mat):
            ones = 0
            for val in row:
                if val == 1:
                    ones += 1
            if ones > best_count:
                best_idx, best_count = i, ones

        return [best_idx, best_count]