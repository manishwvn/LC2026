# Last updated: 8/20/2026, 1:52:46 AM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        vow_counts = Counter()
        cons_counts = Counter()

        for char in s:
            if char in vowels:
                vow_counts[char] += 1
            else:
                cons_counts[char] += 1

        max_vow = max(vow_counts.values(), default=0)
        max_cons = max(cons_counts.values(), default=0)

        return max_vow + max_cons