# Last updated: 8/20/2026, 1:52:20 AM
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        n = len(matrix)
        graph = {}

        for i in range(n):
            graph[i] = []
            for j in range(n):
                if matrix[i][j] == 1:
                    graph[i].append(j)

        res = []
        for node, edges in graph.items():
            res.append(len(edges))

        return res
        