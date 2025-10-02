class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while nums[l] > nums[r]:
            
            # Stop once we've found the rotation boundaries
            if abs(l - r) == 1:
                break

            # Find the middle element
            m = (l + r) // 2
            
            # Check which half of the array is out of order
            if not nums[l] < nums[m]:
                r = m
            else:
                l = m

        return min(nums[l], nums[r])
