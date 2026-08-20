# Last updated: 8/20/2026, 1:55:05 AM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res = []
        
        while nums:
            first, second = heappop(nums), heappop(nums)
            res.append(second)
            res.append(first)

        return res

