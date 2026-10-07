# Last updated: 10/7/2026, 2:44:38 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        myset = set()

        for num in nums:
            if num < k:
                return -1
            if num > k:
                myset.add(num)

        return len(myset)