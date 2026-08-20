# Last updated: 8/20/2026, 1:53:30 AM
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        res = float('inf')
        nums = [0] + nums
        for i in range(l, r + 1):
            for j in range(len(nums) - i):
                subarray_sum = nums[j + i] - nums[j]
                if subarray_sum < res and subarray_sum > 0:
                    res = subarray_sum
        return res if res != float('inf') else -1 