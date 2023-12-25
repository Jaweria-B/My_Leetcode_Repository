class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        global ans
        ans = []
        
        def find(nums, path):
            
            if len(nums) == 0:
                ans.append(path)
                return 
            
            for i in range(len(nums)):
                
                find(nums[: i] +nums[i + 1: ], path + [nums[i]])
                
        find(nums, [])
        
        return ans