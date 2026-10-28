class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        max_xor = 1 << max(max(row) for row in grid).bit_length()

        dp = [[[False] * max_xor for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i == 0 and j == 0:
                    continue

                for v in range(max_xor):
                    prev = v ^ x

                    if i > 0 and dp[i - 1][j][prev]:
                        dp[i][j][v] = True

                    if j > 0 and dp[i][j - 1][prev]:
                        dp[i][j][v] = True

        for v in range(max_xor):
            if dp[m - 1][n - 1][v]:
                return v
