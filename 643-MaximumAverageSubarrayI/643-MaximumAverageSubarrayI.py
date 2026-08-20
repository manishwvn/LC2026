# Last updated: 8/20/2026, 2:10:19 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        
        maxm = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            cur_avg = cur_sum / k
            maxm = max(cur_avg, maxm)
        return maxm