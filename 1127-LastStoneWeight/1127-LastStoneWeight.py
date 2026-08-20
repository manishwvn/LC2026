# Last updated: 8/20/2026, 2:06:16 AM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-weight for weight in stones]
        heapify(heap)

        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)

            if x != y:
                heappush(heap, -(y - x))

        return -heap[0] if heap else 0

        