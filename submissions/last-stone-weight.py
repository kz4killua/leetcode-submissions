import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            d = abs(x - y)
            if d > 0:
                heapq.heappush(heap, -d)

        if len(heap) == 0:
            return 0
        return -heap[0]
