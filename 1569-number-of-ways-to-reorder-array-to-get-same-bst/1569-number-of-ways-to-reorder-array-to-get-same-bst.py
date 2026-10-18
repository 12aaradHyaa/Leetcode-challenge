
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            ways_left = solve(left)
            ways_right = solve(right)

            ways = comb[len(left) + len(right)][len(left)]
            return ways * ways_left % MOD * ways_right % MOD

        return (solve(nums) - 1) % MOD
