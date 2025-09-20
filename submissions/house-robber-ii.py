def _rob(
    current: int, nums: List[int], memo: dict, start: int
):
    # If we started from house 0 and there's more than one
    # house, skip house n - 1
    if (start == 0):
        if (current == len(nums) - 1) and (len(nums) > 1):
            return 0

    if current >= len(nums) - 2:
        return nums[current]

    if (current, start) not in memo:
        output = []
        if current + 2 <= len(nums) - 1:
            output.append(_rob(current + 2, nums, memo, start))
        if current + 3 <= len(nums) - 1:
            output.append(_rob(current + 3, nums, memo, start))
    
        memo[(current, start)] = nums[current] + max(output)

    return memo[(current, start)]


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()

        output = []
        output.append(_rob(0, nums, memo, 0))
        if len(nums) >= 2:
            output.append(_rob(1, nums, memo, 1))
        if len(nums) >= 3:
            output.append(_rob(2, nums, memo, 2))

        return max(output)
