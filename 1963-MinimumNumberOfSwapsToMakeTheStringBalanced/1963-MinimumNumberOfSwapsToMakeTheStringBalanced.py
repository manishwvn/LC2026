# Last updated: 10/7/2026, 2:52:35 PM
class Solution:
    def minSwaps(self, s):
        cur, ans = 0, 0
        for i in s:
            if i == ']' and cur == 0: ans += 1
            if i == '[' or cur == 0: cur += 1
            else: cur -= 1
        return ans