class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (right+left) // 2
            
            if left == right:
                break
            
            if nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid
        
        return left