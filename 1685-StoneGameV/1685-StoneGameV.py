# Last updated: 8/20/2026, 2:01:40 AM
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n < 2:
            return 0

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # ONE n x n table, both triangles used:
        #   dp[i][j], i <= j  ==  maxLeft[i][j]  = max over k in [i..j] of ( f[i][k] + sum(i..k) )
        #   dp[j][i], i <  j  ==  maxRight[i][j] = max over k in [i..j] of ( f[k][j] + sum(k..j) )
        # The shared diagonal is consistent: both equal f[i][i] + stoneValue[i] = stoneValue[i].
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = stoneValue[i]

        answer = 0

        for i in range(n - 1, -1, -1):
            m = i - 1                       # per-row pointer; only ever moves forward
            for j in range(i + 1, n):
                total = prefix[j + 1] - prefix[i]
                target = prefix[i] + prefix[j + 1]   # 2*prefix[k+1] <= target  <=>  left <= right

                # advance to largest k in [i..j-1] with left(k) <= right(k)
                while m + 1 <= j - 1 and 2 * prefix[m + 2] <= target:
                    m += 1

                f = 0
                if m >= i:
                    v = dp[i][m]            # best "keep left" over all valid splits
                    if v > f:
                        f = v

                if m >= i and 2 * prefix[m + 1] == target:
                    start = m               # exact tie at k=m: keeping the right side is also legal
                else:
                    start = m + 1
                if start + 1 <= j:
                    v = dp[j][start + 1]    # best "keep right" over all valid splits
                    if v > f:
                        f = v

                if i == 0 and j == n - 1:
                    answer = f

                cand = f + total
                a = dp[i][j - 1]
                dp[i][j] = cand if cand > a else a       # extend maxLeft along the row
                b = dp[j][i + 1]
                dp[j][i] = cand if cand > b else b       # extend maxRight along the column

        return answer