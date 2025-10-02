class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while True:

            if abs(l - r) <= 1:
                break

            # Get the middle index
            m = (l + r) // 2

            # Narrow the search space
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            else:
                # (The right half is sorted...)
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
