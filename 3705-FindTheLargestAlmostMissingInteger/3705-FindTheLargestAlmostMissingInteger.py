# Last updated: 8/20/2026, 1:53:17 AM
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Fixed-size arrays (not dicts) — O(1) space since bounded by constraint
        first_idx = [-1] * 51
        last_idx = [-1] * 51
        
        # Step 1: Find first and last occurrence of each integer
        for i, num in enumerate(nums):
            if first_idx[num] == -1:
                first_idx[num] = i
            last_idx[num] = i
        
        # Step 2: Find largest integer appearing in exactly 1 subarray
        result = -1
        
        for num in range(51):  # Check all possible values
            if first_idx[num] == -1:
                continue
            
            left = first_idx[num]
            right = last_idx[num]
            
            # Count how many subarrays contain this integer
            count = min(n - k, right) - max(0, left - k + 1) + 1
            
            if count == 1:
                result = max(result, num)
        
        return result