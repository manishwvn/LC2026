# Last updated: 10/7/2026, 2:55:08 PM
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def isSubstring(s, w):
            i, j = 0, 0
            start = 0
            while i < len(s):
                if s[i] == w[j]:
                    i += 1
                    j += 1
                    if j == len(w):
                        return True
                else:
                    start += 1
                    i = start
                    j = 0
            return False

        k = 1
        while isSubstring(sequence, word * k):
            k += 1
        return k - 1