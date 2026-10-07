# Last updated: 10/7/2026, 3:03:18 PM
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3: return False
        i = 0

        while i+1 < len(arr) and arr[i] < arr[i+1]:
                i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        
        while i+1 < len(arr) and arr[i] > arr[i+1]:
            i += 1

        return i == len(arr) - 1
    



        