# Last updated: 8/20/2026, 2:12:24 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        maxm = 0
        zeroes = 0

        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            maxm = max(maxm, r - l + 1)
            r += 1
        return maxm