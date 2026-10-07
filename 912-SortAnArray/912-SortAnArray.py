# Last updated: 10/7/2026, 3:03:36 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1: return nums
        
        heap = []
        result = []
        
        for num in nums:
            heappush(heap, num)
            
            
        while heap:
            result.append(heappop(heap))
            
        return result
        