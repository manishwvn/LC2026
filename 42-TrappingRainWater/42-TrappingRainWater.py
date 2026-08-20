# Last updated: 8/20/2026, 2:19:36 AM
class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0: return 0

        # dp array O(n) space
        result = 0
        l, r = 0, len(height) - 1
        left_wall, right_wall = height[l], height[r]

        while l < r:
            if left_wall < right_wall:
                l += 1
                left_wall = max(left_wall, height[l])
                result += left_wall - height[l]
            else:
                r -= 1
                right_wall = max(right_wall, height[r])
                result += right_wall - height[r]

        return result

            