from typing import List
from functools import lru_cache
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Store original index
        intervals = [
            [start, end, weight, i]
            for i, (start, end, weight) in enumerate(intervals)
        ]

        # Sort by start, then end, etc.
        intervals.sort()

        n = len(intervals)

        # Store all starting points
        starts = [interval[0] for interval in intervals]

        @lru_cache(None)
        def dp(i, count):

            # At most 4 intervals
            if i == n or count == 4:
                return (0, ())

            # Option 1: Skip current interval
            skip_score, skip_indices = dp(i + 1, count)

            start, end, weight, original_index = intervals[i]

            # Find first interval with start > end
            next_i = bisect_right(starts, end)

            # Option 2: Take current interval
            take_score, take_indices = dp(next_i, count + 1)

            # Add current original index
            selected = (original_index,) + take_indices

            # IMPORTANT:
            # Sort indices before comparing lexicographically
            selected = tuple(sorted(selected))

            take_score += weight

            # Take if score is better
            if take_score > skip_score:
                return (take_score, selected)

            # Skip if score is better
            if take_score < skip_score:
                return (skip_score, skip_indices)

            # Same score → lexicographically smaller indices
            return (take_score, min(selected, skip_indices))

        score, indices = dp(0, 0)

        return list(indices)