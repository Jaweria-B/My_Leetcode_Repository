class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        
        nums = nums + nums
        
        ans = [-1]*l
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, i+l):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
            
            counter += 1
            
            if counter == l:
                break
        
        return ans