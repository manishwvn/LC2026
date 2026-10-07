# Last updated: 10/7/2026, 3:04:25 PM
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
            
        