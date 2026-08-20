# Last updated: 8/20/2026, 2:02:55 AM
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        r_min_max = -float("inf")
        for i in range(len(matrix)):
            r_min = min(matrix[i])
            r_min_max = max(r_min_max, r_min)

        c_max_min = float("inf")

        for i in range(len(matrix[0])):
            c_max = max(matrix[j][i] for j in range(len(matrix)))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return [] 

        