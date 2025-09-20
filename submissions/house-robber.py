def _rob(current: int, nums: List[int], memo: dict):
    
    if current >= len(nums) - 2:
        return nums[current]
    
    if current not in memo:
    
        output = []
        if (current + 2) <= (len(nums) - 1):
            output.append(_rob(current + 2, nums, memo))
        if (current + 3) <= (len(nums) - 1):
            output.append(_rob(current + 3, nums, memo))
        memo[current] = nums[current] + max(output)

    return memo[current]


class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = dict()

        output = []
        if 0 <= len(nums) - 1:
            output.append(_rob(0, nums, memo))
        if 1 <= len(nums) - 1:
            output.append(_rob(1, nums, memo))
        return max(output)
