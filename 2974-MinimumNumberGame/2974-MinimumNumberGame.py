# Last updated: 10/7/2026, 2:46:36 PM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res = []
        
        while nums:
            first, second = heappop(nums), heappop(nums)
            res.append(second)
            res.append(first)

        return res

