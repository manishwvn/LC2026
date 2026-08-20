# Last updated: 8/20/2026, 2:03:02 AM
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        cache = {1: 1}
        
        def getPower(n):
            
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = 1 + getPower(n // 2)
                    
                else:
                    cache[n] = 1 + getPower(3 * n + 1)
                    
            return cache[n]
        
        powerMap = [[i, getPower(i)] for i in range(lo, hi+1)]
        
        powerMap.sort(key = lambda x: x[1])
        print(powerMap)
        return powerMap[k-1][0]
                    
                    
        