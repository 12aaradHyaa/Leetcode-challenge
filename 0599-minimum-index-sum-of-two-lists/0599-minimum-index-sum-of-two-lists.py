
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {s: i for i, s in enumerate(list1)}
        ans = []
        min_sum = float('inf')

        for j, s in enumerate(list2):
            if s in indices:
                total = indices[s] + j

                if total < min_sum:
                    min_sum = total
                    ans = [s]
                elif total == min_sum:
                    ans.append(s)

        return ans
