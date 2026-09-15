class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # palindrome[i][j] = True if s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        # dp[i] = maximum number of palindromes
        # using first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i):
                if i - j >= k and palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]