# Last updated: 8/23/2026, 2:26:59 AM
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        present = set(nums)
        result = []
        start = None
        
        for x in range(lower, upper + 1):
            if x not in present:
                if start is None:
                    start = x
            else:
                if start is not None:
                    result.append([start, x - 1])
                    start = None
        
        if start is not None:
            result.append([start, upper])
        
        return result