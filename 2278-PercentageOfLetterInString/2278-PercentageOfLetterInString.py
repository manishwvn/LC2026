# Last updated: 10/7/2026, 2:50:16 PM
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        counts = Counter(s)
        val = counts[letter]
        
        return floor((val / len(s)) * 100)
        
        