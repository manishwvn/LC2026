# Last updated: 10/7/2026, 2:48:53 PM
class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        hm = set([])
        largest = -1
        for num in nums:
            if -num in hm:
                largest = max(largest, abs(num))

            hm.add(num)

        return largest