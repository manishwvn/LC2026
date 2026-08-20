# Last updated: 8/20/2026, 1:54:35 AM
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        counts = Counter()
        l = 0
        max_len = 0

        for r in range(len(s)):
            char = s[r]
            counts[char] += 1

            while counts[char] > 2:
                counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)

        return max_len