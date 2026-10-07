# Last updated: 10/7/2026, 2:50:19 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for num in nums: 
            if abs(num) < abs(answer):
                answer = num
            elif abs(num) == abs(answer):
                answer = max(answer, num)
        return answer