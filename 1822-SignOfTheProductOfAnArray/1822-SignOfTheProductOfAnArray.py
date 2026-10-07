# Last updated: 10/7/2026, 2:53:35 PM
class Solution:
    def arraySign(self, nums: List[int]) -> int:

        sign = 1
        for num in nums:
            if num == 0: return 0
            if num < 0:
                sign *= -1
            
        return sign
        