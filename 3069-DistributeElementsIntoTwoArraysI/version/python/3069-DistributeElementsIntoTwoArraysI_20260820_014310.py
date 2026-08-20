# Last updated: 8/20/2026, 1:43:10 AM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        arr1 = [nums[0]]
4        arr2 = [nums[1]]
5        for i in range(2, len(nums)):
6            if arr1[-1] > arr2[-1]:
7                arr1.append(nums[i])
8            else:
9                arr2.append(nums[i])
10        return arr1 + arr2