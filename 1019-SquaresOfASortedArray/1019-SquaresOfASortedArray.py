# Last updated: 8/20/2026, 2:07:01 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [0] * n
        
        l, r = 0, n - 1
        
        for i in range(n-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                sqr = nums[r]
                r -= 1
                
            else:
                sqr = nums[l]
                l += 1
                
            result[i] = sqr ** 2
            
        return result
        
        