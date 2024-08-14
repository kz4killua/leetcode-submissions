class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        solution = set()
        
        for i, a in enumerate(nums):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while (l < r):

                total = a + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    solution.add((a, nums[l], nums[r]))
                    l += 1
                    while (l < r) and (nums[l] == nums[l - 1]):
                        l += 1

        return list(solution)
