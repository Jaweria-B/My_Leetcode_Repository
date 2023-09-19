class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         Count 

        n = len(nums)
        count = [0] * (n+1)
        
        for i in range(n):
            count[nums[i]] += 1
            if count[nums[i]] > 1:
                return nums[i]
        
        return n