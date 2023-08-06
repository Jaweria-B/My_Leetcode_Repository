class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        # left -> True
        def BinarySearch(nums, target, toFind):
            start = 0
            end = len(nums)-1
            
            ind = -1
            
            while start <= end:
                
                #mid = (start + end)//2
                mid = start + (end - start)//2
                if nums[mid] == target:
                    ind = mid
                    if toFind:  #left
                        end = mid - 1
                    else:  # right
                        start = mid + 1
                        
                elif nums[mid] < target:
                    start = mid + 1
                    
                else:
                    end = mid - 1
                
            return ind
        
        leftMost = BinarySearch(nums, target, True)
        if leftMost == -1:
            return [-1,-1]
        
        rightMost = BinarySearch(nums, target, False)
        
        return [leftMost, rightMost]
        