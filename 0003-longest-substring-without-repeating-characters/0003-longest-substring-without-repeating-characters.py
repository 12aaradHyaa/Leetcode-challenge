class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        maximum = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maximum = max(maximum, right - left + 1)

        return maximum