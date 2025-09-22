# class Solution:
#     """This is the intuitive solution to the problem."""
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         # Multiply all non zero elements, keeping track of all zeros
#         non_zero_product = 1
        
#         zero_indices = set()
#         for i, num in enumerate(nums):
#             if num != 0:
#                 non_zero_product *= num
#             else:
#                 zero_indices.add(i)

#         # Build the result, handling zero values
#         result = []
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 if len(zero_indices) == 1:
#                     result.append(non_zero_product)
#                 else:
#                     result.append(0)
#             else:
#                 if len(zero_indices) == 0:
#                     result.append(non_zero_product // nums[i])
#                 else:
#                     result.append(0)

#         return result


class Solution:
    """This solution solves the problem without using the 
    division operator."""
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Find the products of all elements up to each `i`
        prefixes = [None for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                prefixes[i] = nums[i]
            else:
                prefixes[i] = nums[i] * prefixes[i - 1]

        # Find all products of all elements from each `i`
        suffixes = [None for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                suffixes[i] = nums[i]
            else:
                suffixes[i] = nums[i] * suffixes[i + 1]

        # Build the final outputs
        result = [None for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                result[i] = suffixes[i + 1]
            elif i == (len(nums) - 1):
                result[i] = prefixes[i - 1]
            else:
                result[i] = prefixes[i - 1] * suffixes[i + 1]

        return result
