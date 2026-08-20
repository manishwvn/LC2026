# Last updated: 8/20/2026, 2:07:32 AM
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
        