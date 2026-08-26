class Solution:
    def secondHighest(self, s: str) -> int:
        digits= set()

        for c in s:
             if c.isdigit():
                digits.add(int(c))

        if len(digits) < 2:
            return -1

        digits= sorted(digits)
        return digits[-2]