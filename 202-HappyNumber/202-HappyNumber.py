# Last updated: 8/20/2026, 2:15:58 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_num(num):
            result = 0
            
            while num:
                dig = num % 10
                num //= 10
                result += dig ** 2
            return result
        
        slow, fast = n, next_num(n)
        
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        
        return fast == 1