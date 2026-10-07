# Last updated: 10/7/2026, 2:45:23 PM
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1

        return count
        