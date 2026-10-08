class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            updated = []
            for subset in subsets:
                updated.append(subset)
                updated.append([*subset, num])

            subsets = updated

        return subsets
