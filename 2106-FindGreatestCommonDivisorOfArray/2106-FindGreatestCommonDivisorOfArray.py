# Last updated: 8/20/2026, 1:59:01 AM
class Solution:
    
    def getGCD(self, a, b):
        if b == 0:
            return a
        else:
            return self.getGCD(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        
        a, b = min(nums), max(nums)
        return self.getGCD(a, b)
        