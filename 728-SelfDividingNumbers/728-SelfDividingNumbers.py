# Last updated: 8/20/2026, 2:09:30 AM
class Solution:
    
    def isSelfDiv(self, num: int) -> bool:
        input_num = num
        
        while num:
            rem = num % 10
            
            if rem != 0 and input_num % rem == 0:
                num //= 10
            else:
                return False
        
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        print(self.isSelfDiv(1))
        result = []
        for i in range(left, right + 1, 1):
            if self.isSelfDiv(i):
                result.append(i)
                
        return result
        