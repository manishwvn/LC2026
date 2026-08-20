# Last updated: 8/20/2026, 2:10:17 AM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        curr_sum = sum(nums)
        actual_sum = len(nums) * (len(nums)+1) // 2

        curr_sq_sum = sum(x*x for x in nums)
        actual_sq_sum = len(nums) * (len(nums)+1) * (2 * len(nums) +1) // 6

        diff = curr_sum - actual_sum
        diff_sq = curr_sq_sum - actual_sq_sum
        dm = diff_sq // diff
        d = (diff + dm) // 2
        m = (dm - diff) //2
        return [d, m]
