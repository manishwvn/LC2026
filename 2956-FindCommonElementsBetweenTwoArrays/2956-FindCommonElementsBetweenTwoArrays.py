# Last updated: 10/7/2026, 2:46:41 PM
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        count1, count2 = 0,0
        for num in nums1:
            if num in set2:
                count1 +=1
        for num in nums2:
            if num in set1:
                count2 +=1
        return [count1,count2]