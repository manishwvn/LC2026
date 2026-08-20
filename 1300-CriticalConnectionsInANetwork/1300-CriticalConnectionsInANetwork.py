# Last updated: 8/20/2026, 2:04:32 AM
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = {}
    
        for i in range(n):
            graph[i] = []

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1] * n
        lowest = [0] * n
        time = 0
        result = []

        #dfs
        def dfs(v, u):
            nonlocal time

            if discovery[v] != -1:
                return
            discovery[v] = time
            lowest[v] = time
            time += 1

            for node in graph[v]:
                if node == u:
                    continue
                dfs(node, v)

                if lowest[node] > discovery[v]:
                    result.append([v, node])

                lowest[v] = min(lowest[v], lowest[node])

        dfs(0, 0)

        return result
