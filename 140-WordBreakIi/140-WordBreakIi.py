# Last updated: 8/20/2026, 2:17:08 AM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]  # base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if word in word_set:
                    for prev_sentence in dp[j]:
                        if prev_sentence:
                            dp[i].append(prev_sentence + " " + word)
                        else:
                            dp[i].append(word)

        return dp[n]