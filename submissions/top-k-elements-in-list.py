from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count the frequencies of all elements in 'nums'
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1

        # Use a bucket sort to get the top k elements
        reverse_counts = defaultdict(set)
        for num, count in counts.items():
            reverse_counts[count].add(num)

        output = []
        for i in range(len(nums), -1, -1):
            if reverse_counts[i]:
                output.extend(reverse_counts[i])
                if len(output) >= k:
                    break

        return output
