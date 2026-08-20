# Last updated: 8/20/2026, 1:58:04 AM
class Solution:
    
    def reverseNum(self, num):
        revNum = 0
        
        while num:
            revNum *= 10
            rem = num % 10
            revNum += rem            
            num //= 10
            
        return revNum
        
    
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0:
            return True
        
        inputNum = num
        
        rev1 = self.reverseNum(num)
        print(rev1)
        
        rev2 = self.reverseNum(rev1)
        print(rev2)
        
        return rev2 == inputNum 
        