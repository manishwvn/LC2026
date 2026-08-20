# Last updated: 8/20/2026, 2:00:28 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        counts = Counter(nums)
        res = 0
        for num, count in counts.items():
            if count == 1:
                res += num
        return res
        