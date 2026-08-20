# Last updated: 8/20/2026, 1:52:23 AM
from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        
        # Step 1: Find the 2 smallest unique numbers in O(N) time without sorting
        min1 = min2 = float('inf')
        for num in counts:
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        candidates = []

        # Step 2: Find the smallest valid partner for min1
        best_target_for_min1 = float('inf')
        for num in counts:
            if num > min1 and counts[num] != counts[min1]:
                best_target_for_min1 = min(best_target_for_min1, num)

        if best_target_for_min1 != float('inf'):
            candidates.append([min1, best_target_for_min1])

        # Step 3: Find the smallest valid partner for min2
        if min2 != float('inf'):
            best_target_for_min2 = float('inf')
            for num in counts:
                if num > min2 and counts[num] != counts[min2]:
                    best_target_for_min2 = min(best_target_for_min2, num)

            if best_target_for_min2 != float('inf'):
                candidates.append([min2, best_target_for_min2])

        # Step 4: Return the lexicographically smallest candidate pair
        return min(candidates) if candidates else [-1, -1]