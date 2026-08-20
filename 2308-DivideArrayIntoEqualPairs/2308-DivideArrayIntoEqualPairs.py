# Last updated: 8/20/2026, 1:57:46 AM
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        maxm = max(nums)

        pairs = [False] * (maxm + 1)

        for num in nums:
            pairs[num] = not pairs[num]
        
        for val in pairs:
            if val:
                return False
        
        return True

        