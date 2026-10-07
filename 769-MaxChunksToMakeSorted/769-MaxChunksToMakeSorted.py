# Last updated: 10/7/2026, 3:05:39 PM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_, count = 0, 0 
        
        for i in range(len(arr)):
            max_ = max(max_, arr[i])
            
            if max_ == i:
                count += 1
                
                
        return count