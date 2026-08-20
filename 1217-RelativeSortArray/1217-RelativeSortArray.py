# Last updated: 8/20/2026, 2:05:22 AM
from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        res = []

        # 1. Append elements of arr2 in the specified relative order
        for num in arr2:
            if num in counts:
                for _ in range(counts[num]):
                    res.append(num)
                del counts[num]  # Remove so only unmentioned elements remain

        # 2. Append remaining elements in ascending order
        for num in sorted(counts.keys()):
            for _ in range(counts[num]):
                res.append(num)

        return res