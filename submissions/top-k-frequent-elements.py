class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = dict()
        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1

        top_k = sorted(counts.keys(), key=lambda k: counts[k])
        top_k = list(reversed(top_k))[:k]

        return top_k
        
