# Last updated: 8/20/2026, 1:57:03 AM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                if count > 0:
                    result += (count * (count + 1)) // 2
                    count = 0
        if count > 0:
            result += (count * (count + 1)) // 2

        return result