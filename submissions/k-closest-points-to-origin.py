import heapq
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            d = sqrt(point[0] ** 2 + point[1] ** 2)

            if len(heap) < k:
                heapq.heappush(heap, (-d, point))
            elif d < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-d, point))

        return [entry[1] for entry in heap]
