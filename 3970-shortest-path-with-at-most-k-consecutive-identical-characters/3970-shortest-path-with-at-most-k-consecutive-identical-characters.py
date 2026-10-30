import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        if k < 1:
            return -1

        # State: (node, last character, consecutive count)
        pq = [(0, 0, labels[0], 1)]
        dist = {(0, labels[0], 1): 0}

        while pq:
            cost, u, last_char, count = heapq.heappop(pq)
            state = (u, last_char, count)

            if cost != dist.get(state, float('inf')):
                continue

            if u == n - 1:
                return cost

            for v, weight in graph[u]:
                ch = labels[v]

                if ch == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight
                new_state = (v, ch, new_count)

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, ch, new_count)
                    )

        return -1