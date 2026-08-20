# Last updated: 8/20/2026, 1:57:50 AM
class Solution:
    def digitSum(self, num):
        sumn = 0
        while num:
            rem = num % 10
            sumn += rem
            num //= 10
            
        return sumn
    
    
    def countEven(self, num: int) -> int:
        
        result = 0
        for x in range(1, num+1):
            
            sumn = self.digitSum(x)   
            if sumn % 2 == 0:
                print(x, sumn)
                result += 1
                
        return result
            
        
        
        