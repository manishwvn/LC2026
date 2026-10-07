# Last updated: 10/7/2026, 2:50:59 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos, neg = 0, 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2

        return res

