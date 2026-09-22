class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # pref[node][r] = number of prefixes of this segment
        # whose product % k == r
        pref = [[0] * k for _ in range(4 * n)]

        # Product of the complete segment modulo k
        prod = [1] * (4 * n)

        def merge(node, left, right):
            # Product of the whole segment
            prod[node] = (prod[left] * prod[right]) % k

            # Prefixes completely inside the left segment
            for r in range(k):
                pref[node][r] = pref[left][r]

            # Prefixes that contain all of left segment
            # and then some prefix of right segment
            for r in range(k):
                if pref[right][r] > 0:
                    new_rem = (prod[left] * r) % k
                    pref[node][new_rem] += pref[right][r]

        def build(node, l, r):
            if l == r:
                x = nums[l] % k

                prod[node] = x
                pref[node][x] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def update(node, l, r, index, value):
            if l == r:
                x = value % k

                pref[node] = [0] * k
                pref[node][x] = 1

                prod[node] = x
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            merge(node, node * 2, node * 2 + 1)

        # Query the range [ql, n-1]
        def query(node, l, r, ql):
            if r < ql:
                return None

            if l >= ql:
                return pref[node][:], prod[node]

            mid = (l + r) // 2

            left_result = query(node * 2, l, mid, ql)
            right_result = query(node * 2 + 1, mid + 1, r, ql)

            if left_result is None:
                return right_result

            if right_result is None:
                return left_result

            left_pref, left_prod = left_result
            right_pref, right_prod = right_result

            merged_pref = [0] * k

            # Prefixes entirely in left part
            for r in range(k):
                merged_pref[r] += left_pref[r]

            # Prefixes containing all of left part
            # followed by a prefix of right part
            for r in range(k):
                if right_pref[r] > 0:
                    new_rem = (left_prod * r) % k
                    merged_pref[new_rem] += right_pref[r]

            merged_prod = (left_prod * right_prod) % k

            return merged_pref, merged_prod

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists for future queries
            update(1, 0, n - 1, index, value)

            # We only need prefixes of nums[start:]
            counts, _ = query(1, 0, n - 1, start)

            answer.append(counts[x])

        return answer