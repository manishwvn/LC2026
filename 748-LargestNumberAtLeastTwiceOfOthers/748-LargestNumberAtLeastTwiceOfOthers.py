# Last updated: 8/20/2026, 2:09:16 AM
class Solution:

  def dominantIndex(self, nums: List[int]) -> int:
    first = -1
    second = -1
    max_idx = -1

    for i, num in enumerate(nums):
      if num > first:
        second = first
        first = num
        max_idx = i
      elif num > second:
        second = num

    return max_idx if first >= 2 * second else -1