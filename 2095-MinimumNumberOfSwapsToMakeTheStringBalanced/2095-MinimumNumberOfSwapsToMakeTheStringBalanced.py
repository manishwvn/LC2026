# Last updated: 8/20/2026, 1:59:08 AM
class Solution:
    def minSwaps(self, s):
        cur, ans = 0, 0
        for i in s:
            if i == ']' and cur == 0: ans += 1
            if i == '[' or cur == 0: cur += 1
            else: cur -= 1
        return ans