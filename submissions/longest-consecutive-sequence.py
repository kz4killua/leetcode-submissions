class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashnums = set(nums)

        # Check which elements start a sequence
        roots = set()
        for num in hashnums:
            if (num - 1) not in hashnums:
                roots.add(num)

        # Count up all sequences
        lengths = dict()
        for root in roots:
            lengths[root] = 1

            num = root + 1
            while num in hashnums:
                lengths[root] += 1
                num += 1

        return max(lengths.values(), default=0)
