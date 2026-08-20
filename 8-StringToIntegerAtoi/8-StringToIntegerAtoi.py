# Last updated: 8/20/2026, 2:20:34 AM
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        result *= sign

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result