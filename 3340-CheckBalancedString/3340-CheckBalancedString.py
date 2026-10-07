# Last updated: 10/7/2026, 2:44:23 PM
class Solution:
    def isBalanced(self, num: str) -> bool:
        
        odd, even = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])

        return odd == even

