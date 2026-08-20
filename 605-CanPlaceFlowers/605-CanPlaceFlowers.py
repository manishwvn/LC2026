# Last updated: 8/20/2026, 2:10:54 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if not n: return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                    
        return False
        