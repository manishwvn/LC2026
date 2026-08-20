# Last updated: 8/20/2026, 2:17:25 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr += 1
                longest = max(curr, longest)
        return longest
