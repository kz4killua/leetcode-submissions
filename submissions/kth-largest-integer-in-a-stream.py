import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # Initialize the fixed-size min-heap
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If the heap is not full, add more items
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
