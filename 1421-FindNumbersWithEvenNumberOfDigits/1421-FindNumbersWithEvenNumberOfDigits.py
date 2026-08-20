# Last updated: 8/20/2026, 2:03:39 AM
class Solution:
    
    def countDigits(self, num):
        counts = 0
        
        while num:
            counts += 1
            num //= 10
        return counts
    
    def findNumbers(self, nums: List[int]) -> int:
        
        result = 0
        for num in nums:
            counts = self.countDigits(num)
            if counts % 2 == 0:
                result += 1
        
        return result
        