# Last updated: 10/7/2026, 2:52:24 PM
class Solution:
    
    def getGCD(self, a, b):
        if b == 0:
            return a
        else:
            return self.getGCD(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        
        a, b = min(nums), max(nums)
        return self.getGCD(a, b)
        