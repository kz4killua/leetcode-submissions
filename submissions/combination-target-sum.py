class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination_sum(nums, target, 0, [], combinations)
        return combinations


def combination_sum(
    nums: list[int],
    target: int,
    i: int,
    current: list[int],
    combinations: list,
):
    if i >= len(nums):
        return

    if target < 0:
        return

    if target == 0:
        combinations.append(current)
        return

    # Case 1: Include nums[i]. Do not advance.
    combination_sum(nums, target - nums[i], i, [*current, nums[i]], combinations)
    # Case 2: Do not include nums[i]. Advance.
    combination_sum(nums, target, i + 1, current, combinations)
