# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        length = mountain_arr.length()
        
        # 1. Find the index of the peak element
        
        low = 1
        high = length - 2
        
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        peak_index = low
        
        
        # 2. Search in  the strickly increasing part 
        
        low = 0
        high = peak_index
        
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index 
        
        if mountain_arr.get(low) == target:
            return low
        
        # 3. Otherwise, check in the stricktly decreasing part
        
        low = peak_index + 1
        high = length - 1
        
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        
        if mountain_arr.get(low) == target:
            return low
        
        
        # Target is not present in the array
        return -1