# Last updated: 8/20/2026, 1:57:25 AM
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        counts = Counter(s)
        val = counts[letter]
        
        return floor((val / len(s)) * 100)
        
        