# Last updated: 10/7/2026, 2:48:27 PM
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)

        for road in roads:
            src, dest, dist = road
            graph[src].append([dest, dist])
            graph[dest].append([src, dist])

        visited = set()
        visited.add(1)
        result = float('inf')
        queue = deque([1])

        while queue:
            node = queue.popleft()

            for dest, weight in graph[node]:
                result = min(result, weight)
                if dest not in visited:
                    visited.add(dest)
                    queue.append(dest)

        return result