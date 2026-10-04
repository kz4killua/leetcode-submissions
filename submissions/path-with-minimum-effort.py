import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        source = (0, 0)
        target = (rows - 1, cols - 1)

        distances = {
            (r, c): float("inf") 
            for r in range(rows) 
            for c in range(cols)
        }
        distances[source] = 0

        heap = [(distances[source], source)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > distances[u]:
                continue

            for v in [
                (u[0] + 1, u[1]),
                (u[0] - 1, u[1]),
                (u[0], u[1] + 1),
                (u[0], u[1] - 1),
            ]:
                if not (0 <= v[0] < rows):
                    continue
                if not (0 <= v[1] < cols):
                    continue

                new_distance = max(
                    distances[u], 
                    abs(heights[u[0]][u[1]] - heights[v[0]][v[1]])
                )
                if distances[v] > new_distance:
                    distances[v] = new_distance

                    heapq.heappush(heap, (distances[v], v))

        return distances[target]
