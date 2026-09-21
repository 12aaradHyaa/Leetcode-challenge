class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[num % k] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * (num % k)) % k
                    new_dp[new_r] += dp[r]

            # All subarrays ending here
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result