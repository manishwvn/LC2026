# Last updated: 8/20/2026, 2:09:57 AM
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        curr, max_len = 0, 0

        for i, num in enumerate(nums):
            if i == 0 or nums[i-1] >= nums[i]:
                curr = 1

            else:
                curr += 1

            max_len = max(curr, max_len)
        
        return max_len
        
        