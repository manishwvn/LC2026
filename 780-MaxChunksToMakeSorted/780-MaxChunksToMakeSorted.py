# Last updated: 8/20/2026, 2:09:06 AM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_, count = 0, 0 
        
        for i in range(len(arr)):
            max_ = max(max_, arr[i])
            
            if max_ == i:
                count += 1
                
                
        return count