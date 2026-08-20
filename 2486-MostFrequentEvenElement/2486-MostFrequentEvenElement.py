# Last updated: 8/20/2026, 1:56:39 AM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] % 2 == 0:
                return nums[0]
            else:
                return -1
            
        hm = {}
        for num in nums:
            if num % 2 == 0:
                if num in hm:
                    hm[num] += 1
                else:
                    hm[num] = 1
                    
        if not hm:
            return -1
        
        count = -1
        result = []
        for i in hm:
            if hm[i] > count:
                count = hm[i]
                
        for k, v in hm.items():
            if v == count:
                result.append(k)
                
        return min(result)
        
        