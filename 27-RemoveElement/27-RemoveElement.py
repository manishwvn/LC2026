# Last updated: 8/20/2026, 2:19:59 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1

            else:
                i += 1

        return n 
        