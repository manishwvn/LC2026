# Last updated: 10/7/2026, 2:46:59 PM
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_idx = max_idx = 0
        
        for i in range(indexDifference, len(nums)):
            j = i - indexDifference
            
            # Track the smallest and largest values seen so far (within valid range)
            if nums[j] < nums[min_idx]:
                min_idx = j
            if nums[j] > nums[max_idx]:
                max_idx = j
            
            # Check against both extremes
            if nums[i] - nums[min_idx] >= valueDifference:
                return [min_idx, i]
            if nums[max_idx] - nums[i] >= valueDifference:
                return [max_idx, i]
        
        return [-1, -1]