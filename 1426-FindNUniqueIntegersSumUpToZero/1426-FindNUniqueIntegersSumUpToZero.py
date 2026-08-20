# Last updated: 8/20/2026, 2:03:37 AM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n < 1:
            return [0]
        
        result = []
        if n % 2 != 0:
            for i in range(-(n // 2), (n // 2) + 1, 1):
                result.append(i)
        else:
            for i in range(-(n // 2), (n // 2) + 1, 1):
                if i != 0:
                    result.append(i)
                    
        return result
            
            
        