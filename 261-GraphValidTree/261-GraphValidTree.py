# Last updated: 8/20/2026, 2:14:50 AM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        graph = {}

        for i in range(n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        stack = []

        stack.append(0)

        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
                graph[neighbor].remove(node)

        return len(visited) == n
        