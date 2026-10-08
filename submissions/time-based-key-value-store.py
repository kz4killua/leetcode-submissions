from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = dict()
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key, timestamp)] = value
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.store:
            return self.store[(key, timestamp)]

        if len(self.times[key]) == 0:
            return ""

        # Run a binary search on the list of times for that key
        key_timestamps = self.times[key]

        lo = 0
        hi = len(key_timestamps) - 1

        while lo != hi:
            mid = (lo + hi + 1) // 2
            mid_timestamp = key_timestamps[mid]

            if mid_timestamp <= timestamp:
                lo = mid
            else:
                hi = mid - 1

        best_timestamp = key_timestamps[lo]
        if best_timestamp > timestamp:
            return ""

        return self.store[(key, best_timestamp)]
