# Last updated: 8/20/2026, 2:11:31 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sumn = 0
        prefix_sum = {0:1}

        for num in nums:
            sumn += num

            if sumn - k in prefix_sum:
                count += prefix_sum[sumn - k]

            if sumn in prefix_sum:
                prefix_sum[sumn] += 1
            
            else:
                prefix_sum[sumn] = 1

        return count