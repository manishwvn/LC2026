# Last updated: 8/20/2026, 2:02:22 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_num, max_sec = 0, 0

        for num in nums:
            if num > max_num:
                max_sec = max_num
                max_num = num
            else:
                max_sec = max(max_sec, num)

        return (max_num - 1) * (max_sec - 1)