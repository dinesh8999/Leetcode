class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word:
                    dp[i] = True
                    break
        return dp[n]


        