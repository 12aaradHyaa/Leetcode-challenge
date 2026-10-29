
from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_update(l, r, value):
            add(l, value)
            if r < n:
                add(r, value)

        chars = list(s)

        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            range_update(tin[u], tout[u], mask)

        def get_mask(u):
            return prefix(tin[u] + 1)

        answer = []

        for q in queries:
            parts = q.split()
            operation = parts[0]
            u = int(parts[1])

            if operation == "update":
                c = parts[2]
                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                if old_mask != new_mask:
                    range_update(tin[u], tout[u], old_mask ^ new_mask)
                    chars[u] = c

            else:
                v = int(parts[2])
                w = lca(u, v)

                path_mask = get_mask(u) ^ get_mask(v)
                path_mask ^= 1 << (ord(chars[w]) - ord('a'))

                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer
