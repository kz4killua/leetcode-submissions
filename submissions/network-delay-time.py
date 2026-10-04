import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Use a hashmap for O(1) lookups of node neighbors
        nodes = [i + 1 for i in range(n)]
        
        neighbors = {node: [] for node in nodes}
        for ui, vi, ti in times:
            neighbors[ui].append((vi, ti))

        # Run Dijkstra's algorithm to get shortest times for each node
        times = {node: float('inf') for node in nodes}
        times[k] = 0
        heap = [(times[k], k)]

        while heap:
            u_time, u = heapq.heappop(heap)

            if u_time > times[u]:
                continue

            for v, t in neighbors[u]:
                new_time = u_time + t
                if times[v] > new_time:
                    times[v] = new_time
                    heapq.heappush(heap, (times[v], v))

        # Return the minimum time it takes for all nodes to receive the signal
        output = 0
        for node, time in times.items():
            if time == float('inf'):
                return -1
            output = max(output, time)

        return output
