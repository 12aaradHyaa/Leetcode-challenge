class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            add = (total - dp[i] + 1) % MOD

            total = (total + add) % MOD
            dp[i] = (dp[i] + add) % MOD

        return total