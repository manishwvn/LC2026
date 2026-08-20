# Last updated: 8/20/2026, 1:53:42 AM
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        prefix_left = [0] * len(nums)
        prefix_left[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_left[i] = nums[i] + prefix_left[i-1]

        print(prefix_left)
        
        prefix_right = [0] * len(nums)
        prefix_right[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            prefix_right[i] = nums[i] + prefix_right[i+1]

        print(prefix_right)

        result = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            
            left_sum = prefix_left[i]
            right_sum = prefix_right[i]

            if left_sum == right_sum:
                result += 2
            
            if left_sum == right_sum + 1 or right_sum == left_sum + 1:
                result += 1

        return result


        