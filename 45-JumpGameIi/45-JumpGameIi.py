# Last updated: 8/20/2026, 2:19:31 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        result = 0
        r = 0
        far = 0
        
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            
            if i == r:
                result += 1
                r = far
                
        return result
        