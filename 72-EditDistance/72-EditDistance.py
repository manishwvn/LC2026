# Last updated: 8/20/2026, 2:18:46 AM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        m, n = len(word1), len(word2)
        
        dp = [0] * (n+1)
        
        for j in range(n+1):
            dp[j] = j
            
        print(dp)
        
        for i in range(1, m+1):
            diagonal = dp[0]
            
            for j in range(0, n+1):
                if j == 0: dp[j] = i
                    
                else:
                    temp = dp[j]
                    if word1[i-1] == word2[j-1]:
                        dp[j] = diagonal
                        
                    else:
                        dp[j] = 1 + min(dp[j], dp[j-1], diagonal)
                        
                    diagonal = temp
                    
        return dp[-1]
                