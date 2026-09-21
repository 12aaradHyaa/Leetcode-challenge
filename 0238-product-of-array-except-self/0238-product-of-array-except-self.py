class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Product of elements to the left
        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Product of elements to the right
        suffix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result