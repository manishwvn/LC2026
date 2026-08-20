# Last updated: 8/20/2026, 2:14:52 AM
class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        
        return num % 9