# Last updated: 8/20/2026, 2:08:10 AM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l, r = 0, len(arr) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if arr[m] > arr[m+1]:
                r = m
                
            else:
                l = m + 1
                
        return l
            
        