# Last updated: 8/20/2026, 2:03:25 AM
class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = 10 ** 9 + 7
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for pick in range(n+1):
            for deliver in range(n+1):
                
                if not pick and not deliver:
                    dp[pick][deliver] = 1
                    continue
                    
                if pick:
                    dp[pick][deliver] += pick * dp[pick-1][deliver]
                    
                dp[pick][deliver] %= mod
                
                
                if deliver > pick:
                    dp[pick][deliver] += (deliver - pick) * dp[pick][deliver - 1]
                    
                dp[pick][deliver] %= mod
                
        return dp[-1][-1]
        