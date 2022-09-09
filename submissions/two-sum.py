class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        checked = dict()
        
        for i in range(len(nums)):
            number = nums[i]
            
            # Have we seen any number that completes the sum?
            remainder = target - number
            if remainder in checked:
                return i, checked[remainder]
            
            # Keep track of all checked values
            checked[number] = i
