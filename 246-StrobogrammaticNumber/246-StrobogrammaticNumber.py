# Last updated: 8/20/2026, 2:15:01 AM
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:    
        numset = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        l, r = 0, len(num) - 1

        
        while l <= r :
            if num[l] not in numset or num[r] not in numset:
                return False
            
            if numset[num[l]] != num[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
        