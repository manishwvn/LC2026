# Last updated: 10/7/2026, 2:48:42 PM
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        nums.sort()
        sum_set = set()

        i, j = 0, len(nums)-1
        
        while i < j:
            sum_set.add(nums[i]+nums[j])
            i += 1
            j -= 1
        
        return len(sum_set)