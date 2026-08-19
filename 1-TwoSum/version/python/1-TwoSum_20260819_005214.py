# Last updated: 8/19/2026, 12:52:14 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        hm = {}
5
6        for i in range(len(nums)):
7            diff = target - nums[i]
8
9            if diff in hm:
10                return [i, hm[diff]]
11
12            hm[nums[i]] = i
13
14        return []
15        