class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        
        # first/last occurrence of every character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # For each character, try to build the smallest valid interval
        # that starts at its first occurrence.
        intervals = []
        for i, c in enumerate(s):
            if first[c] != i:
                continue  # only start a candidate at a char's first occurrence
            
            start, end = i, last[c]
            j = start
            valid = True
            while j <= end:
                cj = s[j]
                # if some character inside needs an occurrence before 'start',
                # this candidate starting at 'start' can never be valid
                if first[cj] < start:
                    valid = False
                    break
                # extend the window to cover this character's last occurrence
                if last[cj] > end:
                    end = last[cj]
                j += 1
            
            if valid:
                intervals.append((start, end))
        
        # Greedily pick max number of non-overlapping intervals:
        # sort by end position, then take smallest end first (classic
        # interval scheduling — works because these intervals are
        # either nested or disjoint, never partially overlapping).
        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        
        return res