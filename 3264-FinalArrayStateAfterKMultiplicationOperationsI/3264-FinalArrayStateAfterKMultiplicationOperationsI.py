# Last updated: 10/7/2026, 2:44:57 PM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        result = nums.copy()

        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            n, i = heapq.heappop(heap)
            result[i] *= multiplier
            heapq.heappush(heap, (result[i], i))

        return result
        