# Last updated: 8/20/2026, 1:57:27 AM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for num in nums: 
            if abs(num) < abs(answer):
                answer = num
            elif abs(num) == abs(answer):
                answer = max(answer, num)
        return answer