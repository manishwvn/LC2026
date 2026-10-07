# Last updated: 10/7/2026, 2:46:39 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_num = max(nums)
        count = 0
        result = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1

            while count == k:
                if nums[l] == max_num:
                    count -= 1
                l += 1
            
            result += l

        return result
