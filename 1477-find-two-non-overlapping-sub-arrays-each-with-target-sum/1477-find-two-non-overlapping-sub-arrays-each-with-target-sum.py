class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [INF] * n

        prefix = 0
        minLength = INF
        answer = INF

        # prefix_sum -> index
        mp = {0: -1}

        for i in range(n):
            prefix += arr[i]

            # Find subarray with sum = target
            if prefix - target in mp:
                j = mp[prefix - target]
                length = i - j

                # Previous subarray must end before j
                if j >= 0 and best[j] != INF:
                    answer = min(answer, best[j] + length)

                minLength = min(minLength, length)

            # Carry previous best
            if i > 0:
                best[i] = best[i - 1]

            best[i] = min(best[i], minLength)

            # Store prefix sum
            mp[prefix] = i

        return -1 if answer == INF else answer