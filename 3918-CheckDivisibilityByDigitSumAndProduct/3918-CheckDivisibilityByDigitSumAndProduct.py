# Last updated: 8/23/2026, 2:27:17 AM
class Solution:
    def checkDivisibility(self, n: int) -> bool:

        sumn, prodn = 0, 1

        temp = n
        while temp:
            digit = temp % 10
            temp //= 10
            sumn += digit
            prodn *= digit

        if n % (sumn + prodn) == 0:
            return True
        else:
            return False