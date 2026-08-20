# Last updated: 8/20/2026, 1:56:02 AM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def bs(x, nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == x:
                    return True
                elif nums[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)

        for num in nums1:
            if bs(num, nums2):
                return num

        return -1
        