# Last updated: 10/7/2026, 2:42:14 PM
class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        dig_freq = [0] * 10

        while n:
            digit = n % 10
            n //= 10
            dig_freq[digit] += 1
        
        score = 0

        for i, freq in enumerate(dig_freq):
            if freq > 0:
                score += i * freq

        return score