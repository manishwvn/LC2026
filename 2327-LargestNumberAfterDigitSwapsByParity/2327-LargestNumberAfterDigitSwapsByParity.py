# Last updated: 8/20/2026, 1:57:35 AM
class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = list(str(num))  # Convert number to list of characters
        odds = sorted([d for d in num_str if int(d) % 2 == 1], reverse=True)
        evens = sorted([d for d in num_str if int(d) % 2 == 0], reverse=True)
        
        result = []
        for digit in num_str:
            if int(digit) % 2 == 0:
                result.append(evens.pop(0))  # Take the largest even
            else:
                result.append(odds.pop(0))  # Take the largest odd
        
        return int("".join(result))  # Convert list back to an integer