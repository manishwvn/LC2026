# Last updated: 8/20/2026, 2:10:25 AM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left, right = 0,int(c ** 0.5)

        while left <= right:

            total = left * left + right * right

            if total == c:
                return True

            elif total > c:
                right -= 1
            else:
                left += 1

        return False
