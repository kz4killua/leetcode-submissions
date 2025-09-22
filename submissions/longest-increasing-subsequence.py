def length_of_lis(nums: List[int], index: int, memo: dict):
    """Find the length of the LIS ending with the 
    element at `index`"""
    if index == 0:
        return 1

    if index not in memo:
    
        # Look backwards for all strictly smaller numbers
        result = 1

        for j in range(index, -1, -1):
            if nums[j] < nums[index]:
                result = max(
                    result, 1 + length_of_lis(nums, j, memo)
                )

        memo[index] = result

    return memo[index]

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = dict()
        
        output = 1
        for i in range(len(nums)):
            output = max(
                output, length_of_lis(nums, i, memo)
            )
        return output
