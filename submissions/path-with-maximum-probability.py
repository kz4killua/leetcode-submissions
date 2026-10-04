import heapq


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:

        neighbors = {node: [] for node in range(n)}
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            neighbors[u].append((v, p))
            neighbors[v].append((u, p))

        probabilities = {node: 0 for node in range(n)}
        probabilities[start_node] = 1.0
        heap = [(-probabilities[start_node], start_node)]
        visited = set()

        while heap:
            _, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)

            if u == end_node:
                return probabilities[u]

            for v, p in neighbors[u]:
                new_prob = probabilities[u] * p

                if new_prob > probabilities[v]:
                    probabilities[v] = new_prob
                    heapq.heappush(heap, (-probabilities[v], v))

        return 0
