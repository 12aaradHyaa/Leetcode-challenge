class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Calculate C(n + k - 1, 2k)
        numerator = 1
        denominator = 1

        for i in range(1, 2 * k + 1):
            numerator = numerator * (n + k - i) % MOD
            denominator = denominator * i % MOD

        # Modular inverse using Fermat's Little Theorem
        return numerator * pow(denominator, MOD - 2, MOD) % MOD