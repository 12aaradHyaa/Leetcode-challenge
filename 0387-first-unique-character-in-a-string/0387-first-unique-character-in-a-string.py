class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency= {}

        for char in s:
            frequency[char]= frequency.get(char, 0)+1

        for i in range (len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1
