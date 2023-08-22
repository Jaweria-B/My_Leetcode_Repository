class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longConsL = 1
        nums_set = set(nums)
        
        for n in nums_set:
            
            if n-1 not in nums_set:
                length = 1
                
                while n+length in nums_set:
                    length += 1
                    longConsL = max(longConsL, length)
        
        return longConsL
        