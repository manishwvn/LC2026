# Last updated: 10/7/2026, 2:42:16 PM
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:

        i, j = 0, len(nums) - 1
        swap = 0
        
        while i < j:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                swap += 1

            elif nums[j] == 0:
                j -= 1

            else:
                i += 1

        return swap

        