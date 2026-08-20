# Last updated: 8/20/2026, 2:16:34 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cand, count = None, 0

        for num in nums:
            if count == 0:
                cand = num
            if num == cand:
                count += 1
            else:
                count -= 1
        
        return cand
        