# Last updated: 8/20/2026, 2:17:13 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        bit = 0
        for num in nums:
            bit ^= num
        
        return bit
            
        