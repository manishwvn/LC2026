# Last updated: 8/20/2026, 2:12:58 AM
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -float('inf')

        for num in nums:
            if num in (first, second, third):
                continue
            
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        return third if third != -float('inf') else first