# Last updated: 10/7/2026, 3:01:52 PM
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

        