class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []

        # Count the number of occurences of each character
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        remaining = {}
        for c in s:
            if not remaining:
                output.append(0)

            if c not in remaining:
                remaining[c] = counts[c]
            remaining[c] -= 1

            output[len(output) - 1] += 1

            if remaining[c] == 0:
                del remaining[c]

        return output
