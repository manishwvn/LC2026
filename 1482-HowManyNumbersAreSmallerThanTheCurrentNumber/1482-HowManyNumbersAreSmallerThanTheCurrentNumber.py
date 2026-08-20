# Last updated: 8/20/2026, 2:03:06 AM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        #counting sort
        maxm = max(nums)
        freq = [0] * (maxm+1)

        for i in range(len(nums)):
            freq[nums[i]] += 1

        cumm_sum = [0] * len(freq)
        roll_sum = 0
        for i in range(len(freq)):
            cumm_sum[i] = roll_sum
            roll_sum += freq[i]

        res = []

        for i in range(len(nums)):
            res.append(cumm_sum[nums[i]])
        return res

        