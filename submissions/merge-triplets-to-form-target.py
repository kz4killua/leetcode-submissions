class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [float("-inf"), float("-inf"), float("-inf")]

        for triplet in triplets:
            merged = [
                max(current[0], triplet[0]),
                max(current[1], triplet[1]),
                max(current[2], triplet[2]),
            ]

            if any(m > t for m, t in zip(merged, target)):
                continue

            current = merged

            if current == target:
                return True

        return False
