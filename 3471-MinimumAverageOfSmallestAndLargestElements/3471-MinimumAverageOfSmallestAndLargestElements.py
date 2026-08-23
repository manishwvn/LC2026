# Last updated: 8/23/2026, 2:27:50 AM
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        averages = []
        nums.sort()

        i, j = 0, len(nums)-1
        while i < j:
            avg = (nums[i] + nums[j]) / 2
            averages.append(avg)
            i += 1
            j -= 1

        averages.sort()
        return averages[0]
        