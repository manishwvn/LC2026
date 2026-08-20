# Last updated: 8/20/2026, 1:53:41 AM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        myset = set()

        for num in nums:
            if num < k:
                return -1
            if num > k:
                myset.add(num)

        return len(myset)