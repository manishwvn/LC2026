# Last updated: 8/20/2026, 2:03:19 AM
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        counts = Counter(arr)
        heap = []
        
        for k, v in counts.items():
            heappush(heap, [-v, k])
            
        result = 0
        n = len(arr)
        m = len(arr)
        
        while n > (m // 2):
            freq, num = heappop(heap)
            print(num)
            n -= counts[num]
            result += 1
            
        return result
            
        
            
        
        
        