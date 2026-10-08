from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo != hi:
            mid = (lo + hi) // 2

            mid_hours = sum(ceil(x / mid) for x in piles)
            if mid_hours <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
