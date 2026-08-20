# Last updated: 8/20/2026, 1:52:13 AM
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