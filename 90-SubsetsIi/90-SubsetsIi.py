# Last updated: 8/20/2026, 2:18:20 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def get_subsets(nums, i, path):
            result.append(path.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                get_subsets(nums, j+1, path)
                path.pop()

        nums.sort()
        result = []
        get_subsets(nums, 0, [])
        return result