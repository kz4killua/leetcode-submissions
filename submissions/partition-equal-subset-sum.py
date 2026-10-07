class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        memo = dict()
        return can_sum(nums, total // 2, 0, memo)


def can_sum(nums: list[int], target: int, i: int, memo: dict):
    """Can we sum a subset of in nums[i:] to hit target?"""
    n = len(nums)
    if i >= n:
        return target == 0

    key = (target, i)

    if key not in memo:
        memo[key] = (
            can_sum(nums, target - nums[i], i + 1, memo) or
            can_sum(nums, target          , i + 1, memo)
        )

    return memo[key]
