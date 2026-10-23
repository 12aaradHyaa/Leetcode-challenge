
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        ans = (1 << 30) - 1
        misplaced = False

        for i in range(n):
            if nums[i] != i:
                ans &= nums[i]
                misplaced = True

        return ans if misplaced else 0
