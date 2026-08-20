# Last updated: 8/20/2026, 2:01:35 AM
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = 0

        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                if (j - i + 1) % 2 == 1:
                    total += sum(arr[i:j+1])
        return total

        