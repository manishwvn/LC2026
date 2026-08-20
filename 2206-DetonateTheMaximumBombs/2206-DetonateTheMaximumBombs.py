# Last updated: 8/20/2026, 1:58:22 AM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        if len(bombs) == 1: return 1

        #build the graph
        n = len(bombs)

        graph = defaultdict(list)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]

                d = (x1 - x2) ** 2 + (y1 - y2)**2
                if d <= r1 ** 2:
                    graph[i].append(j)

        def bfs(i):
            queue = deque()
            visited = set()
            queue.append(i)
            visited.add(i)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return len(visited)


        result = 0
        for i in range(n):
            result = max(result, bfs(i))
        return result
            
        
                
        