# Last updated: 10/7/2026, 2:58:20 PM
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        steps = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1

        return steps
        