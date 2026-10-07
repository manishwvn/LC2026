# Last updated: 10/7/2026, 2:47:57 PM
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        i, j = 0, len(nums)-1
        result = 0
        while i < j:
            result += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        
        if i == j:
            result += nums[i]

        return result