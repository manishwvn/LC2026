# Last updated: 10/7/2026, 2:50:43 PM
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

        