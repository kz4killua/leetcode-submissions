class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals = sorted(intervals)
        merged.append(intervals[0])

        for interval in intervals[1:]:
            last = merged[-1]
            if last[1] >= interval[0]:
                last[0] = min(last[0], interval[0])
                last[1] = max(last[1], interval[1])
            else:
                merged.append(interval)

        return merged
