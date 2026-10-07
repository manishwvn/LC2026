# Last updated: 10/7/2026, 2:43:06 PM
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