class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
       
        l,r = 0, 0
        ans = []
        while r < len(nums):
            while r + 1 < len(nums) and nums[r+1] == nums[r]+1:
                r += 1
            
            if l == r:
                ans.append(str(nums[l]))
            else:
                ans.append(str(nums[l]) + "->" + str(nums[r]))
            r += 1
            l = r
        
        return ans
    
    
    
    
    
    
#         if len(nums) == 0:
#             return []
        
#         ans = []
#         temp = 0
#         for i in range(0, len(nums)):
#             while i + 1 < len(nums) and nums[i+1] == nums[i] + 1 :
#                 i += 1
#                 print(temp, i)
#             if temp != i:
#                 val = str(nums[temp]) + "->" + str(nums[i])
#                 ans.append(val)
#             else:
#                 ans.append(str(nums[i]))
#             temp = i + 1
#         return ans