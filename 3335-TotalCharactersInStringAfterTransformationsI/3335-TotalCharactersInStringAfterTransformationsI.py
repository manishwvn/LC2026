# Last updated: 10/7/2026, 2:44:24 PM
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for j in range(t):
            new_freq = [0] * 26

            for i in range(26):
                if i == 25:
                    new_freq[0] = (new_freq[0] + freq[25]) % mod
                    new_freq[1] = (new_freq[1] + freq[25]) % mod
                else:
                    new_freq[i+1] = (new_freq[i+1] + freq[i]) % mod
            freq = new_freq
            
        return sum(freq) % mod