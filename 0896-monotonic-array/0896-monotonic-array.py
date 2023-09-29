class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        direction = 0
            
        i = 1
        while i < len(nums):
            
            if nums [i] > nums[i-1]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
                
            elif nums[i] < nums[i-1]:
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False
            i += 1
        
        return True