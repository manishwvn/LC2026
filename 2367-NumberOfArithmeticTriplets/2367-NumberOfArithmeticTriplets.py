# Last updated: 10/7/2026, 2:49:34 PM
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        s = set(nums)
        
        for num in nums:
            if num + diff in s and num + diff + diff in s:
                count += 1
        return count
        