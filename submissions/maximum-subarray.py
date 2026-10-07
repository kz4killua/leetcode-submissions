class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        maximum_sum = nums[0]

        for num in nums[1:]:
            if current_sum + num < num:
                current_sum = 0
            current_sum += num

            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum
