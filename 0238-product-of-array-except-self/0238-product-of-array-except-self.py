class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n
        pre = 1
        post = 1
        
        for i in range(n):
            
            answer[i] *= pre
            pre *= nums[i]
            
            answer[n-i-1] *= post
            post *= nums[n-i-1]
            
        return answer