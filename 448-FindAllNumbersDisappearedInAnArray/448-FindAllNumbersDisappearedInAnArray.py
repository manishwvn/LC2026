# Last updated: 8/20/2026, 2:12:37 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [False] * (n + 1)
        for num in nums:
            counts[num] = True 
        return [i for i in range(1, n + 1) if counts[i] == False]