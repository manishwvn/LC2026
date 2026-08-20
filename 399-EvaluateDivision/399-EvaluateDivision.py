# Last updated: 8/20/2026, 2:13:10 AM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
    
        for i in range(len(equations)):
            num, den = equations[i]

            if num not in graph:
                graph[num] = {}

            if den not in graph:
                graph[den] = {}

            graph[num][den] = values[i]
            graph[den][num] = 1/values[i]

        print(graph)    
        result = []
    
    
    
        def dfs(start, end, prod, visited):
            visited.add(start)
            val = -1.0

            neighbors = graph[start]

            if end in neighbors:
                val = prod * neighbors[end]

            else:
                for neighbor, weight in neighbors.items():
                    if neighbor in visited:
                        continue
                    val = dfs(neighbor, end, prod * weight, visited)

                    if val != -1.0:
                        break

            visited.remove(start)
            return val
        
        
        
    
        for query in queries:
            num, den = query
            if num not in graph or den not in graph:
                result.append(-1.0)

            elif num == den:
                result.append(1.0)

            else:
                visited = set()
                val = dfs(num, den, 1, visited)
                result.append(val)

        return result
        